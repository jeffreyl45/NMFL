"""# Step 1: Create & activate virtualenv
python3 -m venv langgraph-demo
source langgraph-demo/bin/activate

# Step 2: Upgrade pip (optional, but helpful)
pip install --upgrade pip

# Step 3: Install all dependencies
pip install -r requirements.txt

# Step 4: (Only once) Pull a model with Ollama
curl -fsSL https://ollama.com/install.sh | sh
ollama pull mistral  # or llama3, etc.

# Step 5: Run your LangGraph app
python main.py
"""

# main.py
# main.py
# LangGraph: language -> (pronunciation & grammar) -> final
# Backend: Ollama (mistral). Make sure `ollama serve` is running and you've done `ollama pull mistral`.

from typing import TypedDict, Optional
from langchain_ollama import ChatOllama
from langgraph.graph import StateGraph, END

# ---------- Shared state ----------
class GraphState(TypedDict):
    input: str                     # user sentence (read-only once set)
    language: Optional[str]        # set by language_node
    pronunciation: Optional[str]   # set by pronunciation_node
    analysis: Optional[str]        # set by grammar_node
    output: Optional[str]          # set by final_node

llm = ChatOllama(model="mistral", temperature=0)

# ---------- Parent: detect language ----------
def language_node(state: GraphState) -> dict:
    prompt = (
        "Detect the language of this sentence. Reply with the language name only "
        "(e.g., French, English, Korean).\n\n"
        f"Sentence: {state['input']}"
    )
    res = llm.invoke(prompt)
    return {"language": res.content.strip()}

# ---------- Child 1: pronunciation ----------
def pronunciation_node(state: GraphState) -> dict:
    prompt = (
        "You are a pronunciation coach. For the sentence, provide:\n"
        "1) An approximate IPA or phonetic guide\n"
        "2) A syllable breakdown\n"
        "3) Stress pattern (if relevant)\n"
        "4) One or two mouth/tongue tips\n\n"
        f"Language: {state.get('language','(unknown)')}\n"
        f"Sentence: {state['input']}"
    )
    res = llm.invoke(prompt)
    return {"pronunciation": res.content.strip()}

# ---------- Child 2: grammar & context ----------
def grammar_node(state: GraphState) -> dict:
    prompt = (
        "You are a multilingual tutor. For the sentence, provide:\n"
        "1) An English translation (or say it's already English)\n"
        "2) A brief word-by-word gloss (parts of speech / particles)\n"
        "3) Key grammar points (tense, agreement, idioms, register)\n"
        "4) One short usage/nuance tip\n\n"
        f"Language: {state.get('language','(unknown)')}\n"
        f"Sentence: {state['input']}"
    )
    res = llm.invoke(prompt)
    return {"analysis": res.content.strip()}

# ---------- Final: join & compose ----------
def final_node(state: GraphState) -> dict:
    # Only emit once both branches have produced results
    if not state.get("pronunciation") or not state.get("analysis"):
        return {}  # no-op until both are present

    merged = (
        f"## Language: {state.get('language','Unknown')}\n\n"
        f"### Pronunciation\n{state['pronunciation']}\n\n"
        f"### Context & Grammar\n{state['analysis']}"
    )
    return {"output": merged}

# ---------- Build graph: language -> (pronunciation & grammar) -> final ----------
builder = StateGraph(GraphState)
builder.add_node("language", language_node)
builder.add_node("pronunciation", pronunciation_node)
builder.add_node("grammar", grammar_node)
builder.add_node("final", final_node)

builder.set_entry_point("language")
# fan-out to children
builder.add_edge("language", "pronunciation")
builder.add_edge("language", "grammar")
# join at final
builder.add_edge("pronunciation", "final")
builder.add_edge("grammar", "final")
builder.add_edge("final", END)

app = builder.compile()

if __name__ == "__main__":
    while True:
        text = input("\nEnter a sentence (or 'q' to quit): ").strip()
        if not text or text.lower() in {"q", "quit", "exit"}:
            break

        # Set read-only inputs once; children never write to these keys
        init: GraphState = {
            "input": text,
            "language": None,
            "pronunciation": None,
            "analysis": None,
            "output": None,
        }

        out = app.invoke(init)
        print("\n" + (out.get("output") or "No output produced."))
