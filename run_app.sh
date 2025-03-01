#!/bin/bash

# Get local IP address
ip_address=$(hostname -I | awk '{print $1}')

# Directory of the script
DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"

# Activate the virtual environment
source "$DIR/venv/bin/activate"

# Make sure requests module is installed for the direct API check
pip install requests > /dev/null 2>&1

# Check if Ollama is running by querying the API
if ! curl -s -m 2 "http://localhost:11434/api/tags" > /dev/null
then
    echo "Ollama is not running. Starting Ollama service..."
    
    # Try to start Ollama in the background
    ollama serve > /dev/null 2>&1 &
    OLLAMA_PID=$!
    
    # Give it a few seconds to start
    echo "Waiting for Ollama to start..."
    for i in {1..10}; do
        if curl -s -m 1 "http://localhost:11434/api/tags" > /dev/null; then
            echo "Ollama started successfully!"
            break
        fi
        
        if [ $i -eq 10 ]; then
            echo "Failed to start Ollama after waiting. Please start Ollama manually with 'ollama serve' command."
            echo "Killing the attempted Ollama process..."
            kill $OLLAMA_PID 2>/dev/null
            exit 1
        fi
        
        echo "Waiting... ($i/10)"
        sleep 2
    done
fi

# Check if there are any models
if ! curl -s "http://localhost:11434/api/tags" | grep -q "models"; then
    echo "Warning: No models found in Ollama."
    echo "Consider pulling a model with: ollama pull deepseek-r1:8b"
fi

# Print access information
echo "==============================================="
echo "Starting Streamlit app at http://$ip_address:8501"
echo "Access from another device using this URL"
echo "==============================================="

# Run the Streamlit app
cd "$DIR"
streamlit run app.py --server.address=0.0.0.0