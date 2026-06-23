from pydantic import BaseModel, Field
from typing import Literal, Optional, Any
from langchain_groq import ChatGroq
from langchain_openai import ChatOpenAI
from langchain_ollama import ChatOllama
from utils.config_loader import load_config
import os

class ConfigLoader:
    def __init__(self):
        print('Loading Config')
        self.config = load_config()

    def __getitem__(self, key):
        return self.config[key] 

class ModelLoader(BaseModel):
    model_provider: Literal['groq', 'openrouter', 'ollama'] = 'groq'
    config: Optional[ConfigLoader] = Field(default=None, exclude=True)

    def model_post_init(self, __config: Any) -> None:
        self.config = ConfigLoader()

    class Config:
        arbitrary_types_allowed = True

    def load_llm(self):
        """
            Load and return the LLM model.
        """

        print("LLM  loading...")
        print(f"Loading model from provider: {self.model_provider}")

        if self.model_provider == 'groq':
            print('Loading llm from groq')
            groq_api_key = os.getenv('GROQ_API_KEY')
            model = self.config['llm']['groq']['model_name']
            llm = ChatGroq(
                model=model,
                api_key=groq_api_key
            )

        elif self.model_provider == 'openrouter':
            print('Loading llm from openrouter')
            openrouter_api_key = os.getenv('OPENAI_API_KEY')
            model = self.config['llm']['openrouter']['model_name']
            base_url = self.config['llm']['openrouter']['base_url']
            llm = ChatOpenAI(
                model=model,
                api_key=openrouter_api_key,
                base_url=base_url
            )

        elif self.model_provider == 'ollama':
            print('Loading llm from ollama')
            model = self.config['llm']['ollama']['model_name']
            llm = ChatOllama(
                model=model
            )

        else:
            raise ValueError(
                f"Unsupported model provider: {self.model_provider}"
            )

        return llm