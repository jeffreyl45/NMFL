# Language detection node
from .base import BaseNode
from typing import Dict, Any

class LanguageNode(BaseNode):

    def get_prompt(self, state):
        return (
            "Detect the language of this sentence. Reply with the language name only "
            "(e.g., French, English, Korean).\n\n"
            f"Sentence: {state['input']}"
        )

    def process_response(self, response: str) -> Dict[str, Any]:
        return {"language": response}



