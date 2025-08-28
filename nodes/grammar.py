# Grammar analysis node
from .base import BaseNode
from typing import Dict, Any

class GrammarNode(BaseNode):
    def get_prompt(self, state: Dict[str, Any]) -> str:
        return (
        "You are a multilingual tutor. For the sentence, provide:\n"
        "1) An English translation (or say it's already English)\n"
        "2) A brief word-by-word gloss (parts of speech / particles)\n"
        "3) Key grammar points (tense, agreement, idioms, register)\n"
        "4) One short usage/nuance tip\n\n"
        f"Language: {state.get('language','(unknown)')}\n"
        f"Sentence: {state['input']}"
        )

    def process_response(self, response: str) -> Dict[str, Any]:
        return {"grammar": response}
