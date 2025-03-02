# Local LLM Chat with Streamlit and Ollama

A Streamlit application that provides a chat interface for interacting with local LLMs running through Ollama.

## Prerequisites

- Ollama installed on your system (visit https://ollama.com/download)
- Python 3.11+ with virtualenv

## Setup

1. Ensure Ollama is installed:
   ```bash
   ./check_ollama.py
   ```

2. The app uses a virtual environment with the following dependencies:
   - streamlit
   - ollama
   - psutil
   - requests
   
   These are already installed in the included venv.

## Running the Application

1. Run the application using the provided script:
   ```bash
   ./run_app.sh
   ```

2. The script will:
   - Check if Ollama is running and attempt to start it if not
   - Start the Streamlit server accessible from other devices on your network
   - Display the URL you can use to access the app from another device

3. Access the application from any device on your local network using the displayed URL.

4. To run with a specific model:
   ```bash
   MODEL_NAME="llama3" ./run_app.sh
   ```

## Features

- Chat interface for interacting with multiple LLM models
- Model selector to switch between available models
- Memory settings to control RAM usage (low, medium, high)
- Automatic model discovery from installed Ollama models
- Stream responses as they're generated
- Conversation history with configurable length
- Option to clear conversation history
- System statistics display
- Keep or clear conversation history when switching models

## Supported Models

The app automatically detects models installed through Ollama. Some recommended models:
- deepseek-r1:8b
- qwen:0.5b
- llama3

To add more models, run in your terminal:
```bash
ollama pull modelname
```

## Memory Management

The app includes memory management features:
- Memory usage presets (low, medium, high)
- Adjustable conversation length limit
- Memory usage statistics display

## Troubleshooting

- If you encounter errors about Ollama not being available, run the check script: `./check_ollama.py`
- Start Ollama manually with `ollama serve` if the auto-start fails
- For other issues, check the Streamlit logs in `streamlit.log`