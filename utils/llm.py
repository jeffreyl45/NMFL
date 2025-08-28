# LLM initialization and configuration utilities
from langchain_ollama import ChatOllama

def get_llm():
    """
    Initialize and return the LLM instance.
    Uses Ollama with Mistral model.
    Make sure `ollama serve` is running and you've done `ollama pull mistral`.
    """
    return ChatOllama(model="mistral", temperature=0)
