# Language detection node
from .base import BaseNode
from typing import Dict, Any

class LanguageNode(BaseNode):

    def get_prompt(self, state: Dict[str, Any]) -> str:
        return (
            "Task: Detect the language of the sentence.\n"
            "Instructions:\n"
            "- Reply with the language name only (e.g., French, English, Korean).\n"
            "- Do not include punctuation, prefixes, confidence scores, or extra words.\n"
            "- If ambiguous, reply exactly: Unknown.\n\n"
            f"Sentence: {state['input']}"
        )

    def process_response(self, response: str) -> Dict[str, Any]:
        return {"language": response}



