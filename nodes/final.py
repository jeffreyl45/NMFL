# Final composition node
from typing import Dict, Any

def final_node(state: Dict[str, Any]) -> Dict[str, Any]:
    """
    Composes all analysis results into final output.
    Only proceeds when all analysis nodes have completed.
    """
    # Check if all required fields are present
    required_fields = ["pronunciation", "grammar", "cultural"]
    if not all(field in state for field in required_fields):
        return {}  # No-op until all analyses are complete
    
    # Compose the final output
    output = (
        f"## Language: {state.get('language', 'Unknown')}\n\n"
        f"### Pronunciation\n{state['pronunciation']}\n\n"
        f"### Grammar & Context\n{state['grammar']}\n\n"
        f"### Cultural Context\n{state['cultural']}"
    )
    
    return {"output": output}
