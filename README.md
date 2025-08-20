# NMFL

## Step 1: Create & activate virtualenv
python3 -m venv langgraph-demo
source langgraph-demo/bin/activate

## Step 2: Upgrade pip (optional, but helpful)
pip install --upgrade pip

## Step 3: Install all dependencies
pip install -r requirements.txt

## Step 4: (Only once) Pull a model with Ollama
curl -fsSL https://ollama.com/install.sh | sh
ollama pull mistral  # or llama3, etc.

## Step 5: Run your LangGraph app
python main.py