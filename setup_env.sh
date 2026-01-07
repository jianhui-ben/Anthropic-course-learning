#!/bin/bash

# Setup script for Claude API learning environment using uv

echo "🚀 Setting up Claude API learning environment with uv..."

# Check if uv is installed
if ! command -v uv &> /dev/null; then
    echo "❌ uv is not installed. Please install it first:"
    echo "   curl -LsSf https://astral.sh/uv/install.sh | sh"
    echo "   or visit: https://docs.astral.sh/uv/getting-started/installation/"
    exit 1
fi

# Create virtual environment with uv
echo "📦 Creating virtual environment..."
uv venv claude-api-env

# Activate the environment and install dependencies
echo "📥 Installing dependencies..."
source claude-api-env/bin/activate
uv pip install -r requirements.txt

# Install ipykernel to make this environment available in Jupyter
echo "🔧 Setting up Jupyter kernel..."
uv pip install ipykernel
python -m ipykernel install --user --name=claude-api-env --display-name="Claude API Learning"

echo "✅ Setup complete!"
echo ""
echo "To use this environment:"
echo "1. Activate it: source claude-api-env/bin/activate"
echo "2. Start Jupyter: jupyter lab"
echo "3. In Jupyter, select 'Claude API Learning' kernel from the kernel menu"
echo ""
echo "Don't forget to create your .env file with your ANTHROPIC_API_KEY!"