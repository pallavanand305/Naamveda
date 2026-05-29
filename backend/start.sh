#!/bin/bash

echo "Starting Naamveda Backend..."
echo ""

# Activate virtual environment
if [ -f "venv/bin/activate" ]; then
    source venv/bin/activate
else
    echo "Virtual environment not found!"
    echo "Please run: python -m venv venv"
    echo "Then run: source venv/bin/activate"
    echo "Then run: pip install -r requirements.txt"
    exit 1
fi

echo "Virtual environment activated!"
echo ""
echo "Starting FastAPI server..."
echo "Backend will be available at: http://localhost:8000"
echo "API Docs will be available at: http://localhost:8000/docs"
echo ""
echo "Press Ctrl+C to stop the server"
echo ""

uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
