import traceback
from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
from agent.agentic_workflow import GraphBuilder

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class QueryRequest(BaseModel):
    query: str

@app.post('/query')
def quer_travel_agent(query: QueryRequest):
    try:
        graph = GraphBuilder( model_provider = 'groq' )
        react_app = graph()

        messages = {
            'messages': [query.query]
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
        traceback.print_exc()
        return JSONResponse( status_code=500, content={ 'error': str(e) } )