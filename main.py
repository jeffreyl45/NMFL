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

from typing import TypedDict, List
from langchain_core.messages import HumanMessage, SystemMessage
from langchain_ollama import ChatOllama
from langgraph.graph import StateGraph, END

# State schema
class GraphState(TypedDict):
    messages: List

# LLM setup (Ollama)
llm = ChatOllama(model="mistral")

# MCP node
def run_chat(state: GraphState) -> GraphState:
    result = llm.invoke(state["messages"])
    return {"messages": state["messages"] + [result]}

# Build graph
builder = StateGraph(GraphState)
builder.add_node("chat", run_chat)
builder.set_entry_point("chat")
builder.add_edge("chat", END)
graph = builder.compile()

# Ask user for input
user_input = input("Enter a sentence (any language): ")

# Run the graph
initial_state = {
    "messages": [
        SystemMessage(content="""
You are a multilingual language-learning assistant. Your job is to:
1. Translate foreign-language sentences into English.
2. Break down each word and grammatical structure clearly.
3. Explain the overall sentence meaning and nuance.
4. If there are any typos in the inputted sentence then highlight and correct it, if there are none say nothing.
5. Show pronounciations beside each part of the sentence that was broken apart.
6. If the sentence is an idiomatic sentence then identify that and describe what it really means.

Be concise but educational. Output should be clear and structured. If the sentence is already in 
English point that out to the user and do nothing more.
"""),
        HumanMessage(content=user_input)
    ]
}
output = graph.invoke(initial_state)

print("\n MCP Output:\n", output["messages"][-1].content)