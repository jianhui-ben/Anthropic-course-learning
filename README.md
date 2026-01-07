# Building with Claude API - Learning Notebooks

A hands-on learning workspace for mastering Anthropic's Claude API through practical examples, interactive notebooks, and real-world implementations.

## What You'll Find Here

This repository demonstrates key Claude API concepts through working code:

- **Interactive Chatbots** - Multi-turn conversations with memory and commands
- **Helper Utilities** - Reusable functions for common Claude API patterns
- **Progressive Learning** - From basic API calls to advanced conversation management
- **Practical Examples** - Ready-to-run scripts and notebook demonstrations

## Quick Start

### Option 1: Automated Setup (Recommended)
```bash
# Run the setup script (creates virtual environment with uv)
./setup_env.sh

# Activate environment and start Jupyter
source claude-api-env/bin/activate
jupyter lab
```

### Option 2: Manual Setup
```bash
# Create virtual environment with uv
uv venv claude-api-env
source claude-api-env/bin/activate

# Install dependencies
uv pip install -r requirements.txt

# Make environment available in Jupyter
uv pip install ipykernel
python -m ipykernel install --user --name=claude-api-env --display-name="Claude API Learning"

# Start Jupyter
jupyter lab
```

### Using the Environment
1. In Jupyter Lab, create a new notebook or open an existing one
2. Click on the kernel name (top right) and select "Claude API Learning"
3. Your notebook will now use the virtual environment with all dependencies

## Learning Path

### 📚 Notebooks (Interactive Learning)
- **`01_getting_started.ipynb`** - Basic API connection and simple chat
- **`02_interactive_chatbot.ipynb`** - Multi-turn conversations with commands and history

### 🛠️ Utilities (`utils/`)
- **`claude_helpers.py`** - Core helper functions for Claude API interactions
  - `get_claude_client()` - Initialize API client with error handling
  - `simple_chat()` - Quick single-message conversations
  - `chat()` - Multi-turn conversation management
  - `add_user_message()` / `add_assistant_message()` - Message history helpers
  - `print_response()` - Formatted response display

### 🎯 Examples (Ready-to-Run)
- **`example_interactive_chatbot.py`** - Full-featured command-line chatbot with:
  - Multi-turn conversation memory
  - Special commands (`history`, `clear`, `quit`)
  - Error handling and graceful exits
  - Demo mode with pre-scripted conversations

### 🧪 Experiments
- Space for quick prototypes and testing new ideas

## Key Features Demonstrated

### 🤖 Interactive Chatbot Capabilities
- **Conversation Memory** - Maintains context across multiple exchanges
- **Command System** - Built-in commands for history, clearing, and navigation
- **Error Handling** - Graceful handling of API errors and user interruptions
- **Flexible Input** - Support for both interactive and demo modes

### 💡 API Best Practices
- **Environment Management** - Secure API key handling with `.env` files
- **Cost Optimization** - Smart model selection (Haiku for learning, Sonnet/Opus when needed)
- **Message Management** - Efficient conversation history tracking
- **Connection Testing** - Robust client initialization with error feedback

### 🔧 Development Patterns
- **Modular Design** - Reusable helper functions in `utils/`
- **Progressive Complexity** - From simple API calls to full applications
- **Documentation** - Clear examples with inline explanations
- **Experimentation** - Safe spaces for testing new ideas

## Running the Examples

### Interactive Chatbot (Command Line)
```bash
source claude-api-env/bin/activate
python examples/example_interactive_chatbot.py
```

Features:
- Type messages to chat with Claude
- Use `history` to see conversation log
- Use `clear` to start fresh
- Use `quit` to exit gracefully

### Jupyter Notebooks
```bash
source claude-api-env/bin/activate
jupyter lab
```

Open any notebook and select the "Claude API Learning" kernel to get started.

## Environment Setup

### Environment Variables

Make sure to set your `ANTHROPIC_API_KEY` environment variable:
```bash
export ANTHROPIC_API_KEY="your-api-key-here"
```

Or create a `.env` file in the root directory:
```bash
cp .env.example .env
# Edit .env and add your actual API key
```

## Virtual Environment Management

This project uses `uv` for fast Python package management and virtual environments.

### Prerequisites
Make sure `uv` is installed:
```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

### Environment Commands
- **Setup**: `./setup_env.sh` (one-time setup)
- **Activate**: `source claude-api-env/bin/activate`
- **Quick activate**: `./activate_env.sh`
- **Deactivate**: `deactivate`

### Jupyter Kernel
After running the setup script, you'll have a "Claude API Learning" kernel available in Jupyter that uses your virtual environment with all dependencies installed.

## Learning Progress

### ✅ Completed
- [x] Basic API connection and authentication
- [x] Simple single-turn conversations
- [x] Multi-turn conversation management
- [x] Interactive chatbot with command system
- [x] Conversation history and memory
- [x] Error handling and graceful exits
- [x] Modular helper function library

### 🎯 Next Steps
- [ ] Function calling capabilities
- [ ] System prompts and role definitions
- [ ] Advanced prompt engineering techniques
- [ ] Rate limiting and cost optimization
- [ ] Integration with external APIs
- [ ] Streaming responses
- [ ] Custom conversation flows

## Tips for Learning

### Cost Management
- Start with `claude-3-haiku-20240307` (cheapest) for experimentation
- Use `claude-3-sonnet-20240229` for more complex tasks
- Reserve `claude-3-opus-20240229` for when you need maximum capability
- Set reasonable `max_tokens` limits (1000-2000 for most experiments)

### Development Workflow
1. **Experiment in notebooks** - Interactive development and testing
2. **Extract to utils** - Move reusable patterns to helper functions
3. **Create examples** - Build standalone scripts demonstrating concepts
4. **Document learnings** - Keep notes of what works and what doesn't

### Troubleshooting
- **API Key Issues**: Check that `.env` file exists and contains valid key
- **Import Errors**: Ensure you're using the "Claude API Learning" kernel in Jupyter
- **Connection Problems**: Test with `01_getting_started.ipynb` first

## Contributing

This is a personal learning repository, but feel free to:
- Fork and adapt for your own learning
- Suggest improvements or additional examples
- Share interesting experiments or discoveries

---

*Happy learning with Claude API! 🚀*