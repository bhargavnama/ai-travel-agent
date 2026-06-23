from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.responses import JSONResponse
from agent.agentic_workflow import GraphBuilder

app = FastAPI()

class QueryRequest(BaseModel):
    query: str

@app.post('/query')
def quer_travel_agent(query: QueryRequest):
    try:
        graph = GraphBuilder( model_provider = 'groq' )
        react_app = graph()

        png_graph = react_app.get_graph().get_mermaid_png()
        with open('my_graph.png', 'wb') as f:
            f.write(png_graph)

        messages = {
            'messages': [query.question]
        }
        output = react_app.invoke(messages)

        if isinstance( output, dict ) and 'messages' in output:
            final_output = output['messages'][-1].content
        else:
            final_output = str(output)

        return {
            'answer': final_output
        }
    except Exception as e:
        return JSONResponse( status_code=500, content={ 'error': str(e) } )