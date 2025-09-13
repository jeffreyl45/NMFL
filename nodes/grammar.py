# Grammar analysis node
from .base import BaseNode
from typing import Dict, Any

class GrammarNode(BaseNode):
    def get_prompt(self, state: Dict[str, Any]) -> str:
        return (
        "Role: Advanced multilingual grammar tutor.\n"
        "Task: Provide precise analysis for an advanced learner.\n"
        "Instructions:\n"
        "- Be specific and concise (max ~10 lines).\n"
        "- If already English, state that explicitly and still analyze grammar/nuance.\n"
        "- Prefer technical terms (tense/aspect/mood, honorifics, particles).\n\n"
        f"Language: {state.get('language','(unknown)')}\n"
        f"Sentence: {state['input']}\n\n"
        "Output format:\n"
        "1) Translation:\n"
        "2) Gloss (word-by-word):\n"
        "3) Key grammar points:\n"
        "4) Register & nuance tip:\n"
        )

    def process_response(self, response: str) -> Dict[str, Any]:
        return {"grammar": response}
