#!/bin/bash

# Quick activation script for the Claude API environment

if [ ! -d "claude-api-env" ]; then
    echo "❌ Virtual environment not found. Run ./setup_env.sh first"
    exit 1
fi

echo "🔄 Activating Claude API environment..."
source claude-api-env/bin/activate

echo "✅ Environment activated!"
echo "You can now run: jupyter lab"