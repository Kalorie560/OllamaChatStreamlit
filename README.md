# Local LLM Chat with Streamlit and Ollama

This is a simple Streamlit application that provides a chat interface for interacting with the deepseek-r1:1.5b model through Ollama.

## Prerequisites

- Ollama installed on your system
- Python 3.11+ with virtualenv

## Setup

1. Ensure Ollama is installed and running:
   ```bash
   ollama serve
   ```

2. The app uses a virtual environment with the following dependencies:
   - streamlit
   - ollama
   - psutil
   
   These are already installed in the included venv.

## Running the Application

1. Start Ollama (in a separate terminal):
   ```bash
   ollama serve
   ```

2. Run the application using the provided script:
   ```bash
   ./run_app.sh
   ```

3. The script will:
   - Check if Ollama is running
   - Start the Streamlit server that's accessible from other devices on your network
   - Display the URL you can use to access the app from another device

4. Access the application from any device on your local network using the displayed URL.

## Features

- Chat interface for interacting with deepseek-r1:1.5b
- Automatic model downloading if not already available
- Stream responses as they're generated
- Conversation history
- Option to clear conversation

## Troubleshooting

- If you encounter errors about Ollama not being available, make sure the Ollama service is running with `ollama serve`
- For other issues, check the Streamlit and Ollama logs for more details