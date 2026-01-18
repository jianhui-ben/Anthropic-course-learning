# Building with Claude API - Learning Notebooks

A hands-on learning workspace for mastering Anthropic's Claude API through practical examples, interactive notebooks, and real-world implementations.

## What You'll Find Here

This repository demonstrates key Claude API concepts through working code:

- **Interactive Chatbots** - Multi-turn conversations with memory, commands, and specialized agents
- **Streaming Responses** - Real-time response generation for dynamic user experiences
- **System Prompts** - Role-based AI agents (math tutor, storyteller, etc.)
- **Helper Utilities** - Comprehensive functions for common Claude API patterns
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
- **`02_interactive_chatbot.ipynb`** - Multi-turn conversations with commands, history, and specialized agents
  - Simple and advanced chatbot implementations
  - Math tutor agent with system prompts
  - Command system (`history`, `clear`, `quit`, `help`)
  - Conversation memory and context management
- **`03_streaming_responses.ipynb`** - Real-time response streaming for dynamic interactions
  - Streaming vs regular response comparison
  - Interactive streaming storyteller
  - Performance and user experience benefits
- **`04_structural_output.ipynb`** - Controlling Claude's output format and structure
  - Stop sequences for precise output control
  - Structured response generation (JSON, code blocks, lists)
  - Prefilling assistant responses for format guidance
  - System prompts for output constraints
- **`05_prompt_eval.ipynb`** - **NEW!** Comprehensive prompt evaluation and testing framework
  - Automated dataset generation for testing prompts
  - LLM-as-a-judge evaluation methodology
  - Syntax validation for structured outputs (JSON, Python, regex)
  - Combined scoring systems (semantic + syntactic evaluation)
  - Movie recommendation prompt testing with real IMDB data
  - Evaluation metrics and performance analysis
- **`06_prompt_engineering.ipynb`** - **NEW!** Advanced prompt engineering with automated evaluation
  - Complete `PromptEvaluator` class for systematic prompt testing
  - Automated test case generation from task descriptions
  - Concurrent evaluation processing for efficiency
  - HTML report generation with detailed scoring breakdowns
  - Template rendering system for dynamic prompt construction
  - Real-world example: Movie recommendation system evaluation

### 🛠️ Utilities (`utils/`)
- **`claude_helpers.py`** - Comprehensive helper functions for Claude API interactions
  - `get_claude_client()` - Initialize API client with error handling
  - `simple_chat()` - Quick single-message conversations
  - `chat()` - Multi-turn conversation management with system prompt support
  - `add_user_message()` / `add_assistant_message()` - Message history helpers
  - `print_response()` - Formatted response display
  - **Enhanced**: Streaming support functions for real-time responses
  - **Enhanced**: Advanced error handling and connection management
  - **Enhanced**: Support for stop sequences and output control

### 🎯 Examples (Ready-to-Run)
- **`example_interactive_chatbot.py`** - Full-featured command-line chatbot with:
  - Multi-turn conversation memory
  - Special commands (`history`, `clear`, `quit`)
  - Error handling and graceful exits
  - Demo mode with pre-scripted conversations

### 📊 Datasets
- **`dataset/dataset.json`** - Curated movie dataset for prompt evaluation
  - 10 popular movies with IMDB IDs
  - Generated using Claude for testing recommendation prompts
  - Used in evaluation frameworks and testing scenarios
- **`dataset/dataset_for_prompt_engineering.json`** - **NEW!** Advanced evaluation dataset
  - 3 diverse test cases for movie recommendation prompts
  - Includes indie films, international cinema, and TV series
  - Comprehensive solution criteria for rigorous evaluation
  - Generated using the PromptEvaluator class

### 🧪 Experiments
- Space for quick prototypes and testing new ideas

## Key Features Demonstrated

### 🤖 Interactive Chatbot Capabilities
- **Conversation Memory** - Maintains context across multiple exchanges
- **Command System** - Built-in commands for history, clearing, and navigation
- **Error Handling** - Graceful handling of API errors and user interruptions
- **Flexible Input** - Support for both interactive and demo modes
- **Specialized Agents** - System prompt-driven role-based AI (math tutor, storyteller)

### 🌊 Streaming Response Features
- **Real-time Output** - See responses generate word-by-word
- **Improved User Experience** - Immediate feedback and perceived faster responses
- **Interactive Applications** - Perfect for chat interfaces and creative tools
- **Performance Comparison** - Side-by-side demos of streaming vs regular responses

### 🎭 System Prompt Mastery
- **Role Definition** - Transform Claude into specialized agents
- **Behavioral Control** - Guide response style, tone, and approach
- **Educational Applications** - Math tutor that guides rather than gives answers
- **Creative Applications** - Storyteller with vivid, engaging narratives

### 🔬 Prompt Evaluation & Engineering
- **Automated Testing Framework** - Systematic evaluation of prompt performance
- **LLM-as-a-Judge** - Use Claude to evaluate Claude's own outputs
- **Multi-Criteria Scoring** - Combine semantic relevance with syntax validation
- **Concurrent Processing** - Efficient batch evaluation with threading
- **HTML Report Generation** - Professional evaluation reports with scoring breakdowns
- **Template System** - Dynamic prompt construction with variable substitution
- **Dataset Generation** - Automated creation of diverse test cases from task descriptions

### 💡 API Best Practices
- **Environment Management** - Secure API key handling with `.env` files
- **Cost Optimization** - Smart model selection (Haiku for learning, Sonnet/Opus when needed)
- **Message Management** - Efficient conversation history tracking
- **Connection Testing** - Robust client initialization with error feedback
- **Temperature Control** - Fine-tuned response creativity and consistency

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

### Prompt Evaluation Framework
```bash
source claude-api-env/bin/activate
jupyter lab
# Open notebooks/06_prompt_engineering.ipynb
```

Features:
- Generate test datasets automatically from task descriptions
- Run systematic evaluations with concurrent processing
- Generate professional HTML reports with scoring breakdowns
- Compare different prompt variations and approaches

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
- [x] **System prompts and role definitions** - Math tutor and storyteller agents
- [x] **Streaming responses** - Real-time response generation
- [x] **Advanced prompt engineering** - Specialized agent behaviors
- [x] **Performance optimization** - Response timing and user experience
- [x] **Prompt evaluation framework** - Automated testing and scoring systems
- [x] **LLM-as-a-judge methodology** - Using Claude to evaluate prompt outputs
- [x] **Concurrent evaluation processing** - Efficient batch testing with threading
- [x] **HTML report generation** - Professional evaluation dashboards

### 🎯 Next Steps
- [ ] Function calling capabilities
- [ ] Advanced conversation flows and branching
- [ ] Rate limiting and cost optimization strategies
- [ ] Integration with external APIs
- [ ] Custom conversation templates
- [ ] Multi-modal interactions (when available)
- [ ] Production deployment patterns
- [ ] A/B testing frameworks for prompt optimization
- [ ] Custom evaluation metrics and scoring systems
- [ ] Integration with prompt management platforms

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