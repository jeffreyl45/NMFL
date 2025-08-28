# Graph construction and compilation logic
from langgraph.graph import StateGraph, END

from models.state import GraphState
from nodes.language import LanguageNode
from nodes.pronunciation import PronunciationNode
from nodes.grammar import GrammarNode
from nodes.cultural import CulturalNode
from nodes.final import final_node

def build_graph():
    """
    Builds and compiles the LangGraph workflow.
    
    Flow:
    language_node -> (pronunciation_node, grammar_node, cultural_node) -> final_node
    """
    builder = StateGraph(GraphState)
    
    # Add all nodes to the graph
    builder.add_node("language", LanguageNode())
    builder.add_node("pronunciation", PronunciationNode())
    builder.add_node("grammar", GrammarNode())
    builder.add_node("cultural", CulturalNode())
    builder.add_node("final", final_node)
    
    # Set the entry point
    builder.set_entry_point("language")
    
    # Fan-out: language detection feeds into all analysis nodes
    builder.add_edge("language", "pronunciation")
    builder.add_edge("language", "grammar")
    builder.add_edge("language", "cultural")
    
    # Fan-in: all analysis nodes feed into the final composition
    builder.add_edge("pronunciation", "final")
    builder.add_edge("grammar", "final")
    builder.add_edge("cultural", "final")
    
    # Final node leads to END
    builder.add_edge("final", END)
    
    return builder.compile()
