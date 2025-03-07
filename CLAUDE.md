# Streamlit Ollama Chat App Guidelines

## Commands
- Run app: `./run_app.sh`
- Run with specific model: `MODEL_NAME="llama3" ./run_app.sh`
- Check Ollama status: `./check_ollama.py`
- Start Ollama service: `ollama serve`
- Install dependencies: `pip install -r requirements.txt`
- Pull new models: `ollama pull model_name`
- Check running models: `ollama list`
- Run tests: `pytest -xvs tests/`

## Code Style
- **Imports**: Standard library first, third-party next, local modules last
- **Naming**: snake_case for functions/variables, UPPER_CASE for constants
- **Types**: Use type hints for function parameters and return values
- **Error Handling**: Use try/except with specific exceptions
- **Streamlit**: Group related UI elements, use session_state for persistence
- **Ollama API**: Handle connection errors gracefully with fallback mechanisms
- **Comments**: Use docstrings for functions, inline for complex logic
- **Formatting**: 4-space indentation, 100 char line limit
- **Functions**: Keep focused on single responsibility with descriptive names