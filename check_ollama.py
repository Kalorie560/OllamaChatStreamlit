#!/usr/bin/env python3
import os
import sys
import requests
import subprocess
import platform
import time

def print_status(message, success=True):
    """Print a status message with color."""
    if success:
        print(f"✅ {message}")
    else:
        print(f"❌ {message}")

def check_ollama_installed():
    """Check if Ollama is installed."""
    try:
        result = subprocess.run(["which", "ollama"], 
                              stdout=subprocess.PIPE, 
                              stderr=subprocess.PIPE, 
                              text=True)
        if result.returncode == 0:
            print_status(f"Ollama is installed at: {result.stdout.strip()}")
            return True
        else:
            print_status("Ollama is not installed or not in PATH", False)
            return False
    except Exception as e:
        print_status(f"Error checking if Ollama is installed: {e}", False)
        return False

def check_ollama_running():
    """Check if Ollama service is running."""
    try:
        response = requests.get("http://localhost:11434/api/tags", timeout=2)
        if response.status_code == 200:
            print_status("Ollama service is running")
            return True
        else:
            print_status(f"Ollama service returned unexpected status: {response.status_code}", False)
            return False
    except requests.exceptions.ConnectionError:
        print_status("Ollama service is not running", False)
        print("   To start Ollama, run: ollama serve")
        return False
    except Exception as e:
        print_status(f"Error checking if Ollama is running: {e}", False)
        return False

def main():
    """Main function to run checks."""
    print("\n=== Ollama Status Check ===\n")
    
    installed = check_ollama_installed()
    if not installed:
        print("\nPlease install Ollama before running this app.")
        print("Visit: https://ollama.com/download")
        return False
    
    running = check_ollama_running()
    if not running:
        return False
    
    print("\n✨ All checks passed! You can now run the app with ./run_app.sh")
    return True

if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1)