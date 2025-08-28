# Cultural analysis node
from .base import BaseNode
from typing import Dict, Any

class CulturalNode(BaseNode):
    def get_prompt(self, state: Dict[str, Any]) -> str:
        return (
            "You are a cultural linguistics expert. Analyze this sentence for cultural context and references:\n"
            "1) Identify any cultural references, idioms, or expressions specific to this language/culture\n"
            "2) Explain the cultural background or origin of these references\n"
            "3) Describe what native speakers would immediately understand vs. what might confuse foreigners\n"
            "4) Suggest cultural equivalents or similar expressions in English/other cultures\n"
            "5) Note any register, formality level, or social context implications\n"
            "6) Highlight generational, regional, or subcultural nuances if present\n\n"
            f"Language: {state.get('language','(unknown)')}\n"
            f"Sentence: {state['input']}\n\n"
            "Focus especially on what makes this sentence culturally authentic and what cultural knowledge is required to truly 'get it'."
        )
    
    def process_response(self, response: str) -> Dict[str, Any]:
        return {"cultural": response}

