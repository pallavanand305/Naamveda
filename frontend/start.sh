#!/bin/bash

echo "Starting Naamveda Frontend..."
echo ""

# Check if node_modules exists
if [ ! -d "node_modules" ]; then
    echo "node_modules not found!"
    echo "Installing dependencies..."
    npm install
    echo ""
fi

echo "Starting Next.js development server..."
echo "Frontend will be available at: http://localhost:3000"
echo ""
echo "Press Ctrl+C to stop the server"
echo ""

npm run dev
