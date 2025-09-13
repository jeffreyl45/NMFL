# Cultural analysis node
from .base import BaseNode
from typing import Dict, Any

class CulturalNode(BaseNode):
    def get_prompt(self, state: Dict[str, Any]) -> str:
        return (
            "Role: Cultural linguistics expert for advanced learners.\n"
            "Task: Analyze cultural references and pragmatic meaning.\n"
            "Instructions:\n"
            "- Focus on idioms, intertextual references, memes, regionalisms, honorifics, politeness systems.\n"
            "- Explain the background concisely; avoid over-generalization.\n"
            "- If none detected, say 'No specific cultural references detected' and explain why.\n\n"
            f"Language: {state.get('language','(unknown)')}\n"
            f"Sentence: {state['input']}\n\n"
            "Output format:\n"
            "1) Cultural references (if any):\n"
            "2) Background / origin:\n"
            "3) Native intuition vs. foreigner pitfalls:\n"
            "4) Register / social context:\n"
            "5) Regional / generational nuance:\n"
            "6) Rough equivalents (EN/other):\n"
        )
    
    def process_response(self, response: str) -> Dict[str, Any]:
        return {"cultural": response}

