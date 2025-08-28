# Pronunciation analysis node
from .base import BaseNode
from typing import Dict, Any


class PronunciationNode(BaseNode):
    def get_prompt(self, state: Dict[str, Any]) -> str:
       return (
        "You are a pronunciation coach. For the sentence, provide:\n"
        "1) An approximate IPA or phonetic guide\n"
        "2) A syllable breakdown\n"
        "3) Stress pattern (if relevant)\n"
        "4) One or two mouth/tongue tips\n\n"
        f"Language: {state.get('language','(unknown)')}\n"
        f"Sentence: {state['input']}"
    )

    def process_response(self, response: str) -> Dict[str, Any]:
        return {"pronunciation": response}

