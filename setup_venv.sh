#!/bin/bash

# Exit immediately if a command exits with a non-zero status
set -e

# Define the virtual environment directory name
VENV_DIR="venv"

# Check if the venv directory exists
if [ ! -d "$VENV_DIR" ]; then
    echo "Virtual environment '$VENV_DIR' not found. Creating it..."
    python3 -m venv "$VENV_DIR"
    
    # Check if requirements.txt exists before attempting installation
    if [ -f "requirements.txt" ]; then
        echo "Installing requirements from requirements.txt..."
        ./"$VENV_DIR"/bin/pip install --upgrade pip
        ./"$VENV_DIR"/bin/pip install -r requirements.txt
    else
        echo "Warning: requirements.txt not found. Skipping package installation."
    fi
else
    source ./venv/bin/activate
    echo "Virtual environment '$VENV_DIR' already exists."
fi

# Optional: activate it automatically