# State definitions for the LangGraph workflow
from typing import TypedDict, Optional

# Single comprehensive state that grows as nodes add data
class GraphState(TypedDict, total=False):
    # Required field - set at initialization  
    input: str
    
    # Optional fields - added by respective nodes
    language: Optional[str]        # Added by language_node
    pronunciation: Optional[str]   # Added by pronunciation_node
    grammar: Optional[str]         # Added by grammar_node  
    cultural: Optional[str]        # Added by cultural_node
    output: Optional[str]          # Added by final_node