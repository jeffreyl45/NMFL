# Base node class for all workflow nodes
from abc import ABC, abstractmethod
from typing import Dict, Any
from utils.llm import get_llm

class BaseNode(ABC):
    def __init__(self):
        self.llm = get_llm()
    
    @abstractmethod
    def get_prompt(self, state: Dict[str, Any]) -> str:
        pass 

    @abstractmethod
    def process_response(self, response: str) -> Dict[str, Any]:
        pass

    def __call__(self, state: Dict[str, Any]) -> Dict[str, Any]:
        prompt = self.get_prompt(state)
        response = self.llm.invoke(prompt)
        return self.process_response(response.content.strip())