#!/bin/bash

echo "This script is not testing under a unix system (Mac and Linux), expect it not working."
echo "Checking for Python 3..."

if command -v python3 >/dev/null 2>&1; then
    echo "Python 3 found. Running main.py..."
    python3 main.py
    exit 0
fi

if command -v python >/dev/null 2>&1; then
    echo "Python found as 'python'. Checking version..."
    python --version

    echo "Attempting to run main.py..."
    python main.py
    exit 0
fi

echo "WARNING: Python 3 is not installed."
echo "This project requires Python 3 to run."
echo "Please install Python 3 from https://www.python.org/"
exit 1