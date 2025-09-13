# Pronunciation analysis node
from .base import BaseNode
from typing import Dict, Any


class PronunciationNode(BaseNode):
    def get_prompt(self, state: Dict[str, Any]) -> str:
       return (
        "Role: Expert pronunciation coach.\n"
        "Task: Provide concise, actionable pronunciation guidance.\n"
        "Instructions:\n"
        "- Keep it under 6 bullet points.\n"
        "- Prefer IPA; if uncertain, give a practical phonetic approximation.\n"
        "- If the sentence is already English, still provide syllable and stress info.\n"
        "- Be specific and avoid generic advice.\n\n"
        f"Language: {state.get('language','(unknown)')}\n"
        f"Sentence: {state['input']}\n\n"
        "Output format:\n"
        "1) IPA / Phonetic:\n"
        "2) Syllables:\n"
        "3) Stress pattern:\n"
        "4) Mouth/Tongue tip:\n"
        "5) Common pitfall:\n"
    )

    def process_response(self, response: str) -> Dict[str, Any]:
        return {"pronunciation": response}

