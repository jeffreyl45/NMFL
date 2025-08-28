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

# main.py - Entry point for the NMFL application
from models.state import GraphState
from graph.builder import build_graph

def main():
    """Main entry point for the NMFL application."""
    # Build the LangGraph workflow
    app = build_graph()
    
    while True:
        text = input("Enter a sentence (or 'q' to quit): ").strip()
        if not text or text.lower() in {"q", "quit", "exit"}:
            print("Goodbye!")
            break

        # Initialize state with user input
        init_state: GraphState = {
            "input": text,
            "language": None,
            "pronunciation": None,
            "grammar": None,
            "cultural": None,
            "output": None,
        }

        try:
            # Run the workflow
            print("Invoking")
            result = app.invoke(init_state)
            print("Finished invoking")
            output = result.get("output")
            
            if output:
                print("\n" + "="*60)
                print(output)
                print("="*60 + "\n")
            else:
                print("\nNo output produced. Please try again.\n")
                
        except Exception as e:
            print(f"\nError processing your input: {e}\n")
            print("Please make sure Ollama is running and the Mistral model is available.")

if __name__ == "__main__":
    main()
