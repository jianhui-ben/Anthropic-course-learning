---
inclusion: always
---

# Claude API Learning Workspace Guidelines

## Purpose
This workspace is dedicated to learning and experimenting with Anthropic's Claude API through hands-on Jupyter notebook exercises. The focus is on rapid experimentation and practical understanding.

## Workspace Philosophy

### Learning-First Approach
- **Experiment freely** - This is a safe space to try things and break them
- **Document discoveries** - Keep notes of what works and what doesn't
- **Iterate quickly** - Don't overthink, just try it
- **Learn by doing** - Practical examples over theoretical knowledge

### Communication Preferences
- **Explanations first** - Provide clear answers and explanations without automatically creating code/files
- **Code on request** - Only write code when explicitly asked to "implement", "create", "show code", "build", etc.
- **Focus on understanding** - Prioritize conceptual clarity over demonstrations unless specifically requested
- **Ask before creating** - When in doubt about whether to write code, ask first

### Notebook Organization Strategy
- **One concept per notebook** - Keep notebooks focused on specific topics
- **Progressive complexity** - Start simple, build up gradually  
- **Reusable patterns** - Extract common code to utils/ for reuse
- **Clear naming** - Use numbered prefixes (01_, 02_) for learning sequence

## Development Patterns

### Quick Experimentation
- Use `simple_chat()` helper for rapid testing
- Create throwaway cells for quick experiments
- Don't worry about perfect code - focus on learning
- Use markdown cells to document insights and learnings

### Code Organization
- **utils/claude_helpers.py** - Common Claude API functions
- **experiments/** - Quick standalone scripts for testing ideas
- **examples/** - Polished examples that demonstrate concepts
- **notebooks/** - Interactive learning and exploration

### API Usage Best Practices
- Always use environment variables for API keys
- Start with cheaper models (Haiku) for experimentation
- Use appropriate max_tokens to control costs
- Test with simple prompts before complex ones

## Recommended Workflow

### Starting a New Topic
1. Create a new numbered notebook in notebooks/
2. Import helper functions from utils/
3. Start with a simple "hello world" style example
4. Build complexity gradually within the same notebook
5. Extract reusable patterns to utils/ when they emerge

### When Experimenting
- Use descriptive markdown headers to organize sections
- Add comments explaining what you're testing
- Keep failed experiments - they're learning opportunities
- Use print statements liberally to understand what's happening

### Cost Management
- Default to claude-3-haiku-20240307 for learning (cheapest)
- Use claude-3-sonnet-20240229 for more complex tasks
- Only use claude-3-opus-20240229 when you need the best performance
- Set reasonable max_tokens limits (1000-2000 for most experiments)

## File Naming Conventions
- Notebooks: `##_descriptive_name.ipynb` (e.g., `01_getting_started.ipynb`)
- Experiments: `experiment_topic.py` (e.g., `experiment_function_calling.py`)
- Examples: `example_use_case.py` (e.g., `example_chatbot.py`)

## Environment Setup Reminders
- Run `./setup_env.sh` for one-time environment setup with uv
- Always activate environment: `source claude-api-env/bin/activate`
- Select "Claude API Learning" kernel in Jupyter notebooks
- Check that .env file exists with ANTHROPIC_API_KEY
- Use virtual environment to avoid dependency conflicts

## Learning Goals Tracking
Keep track of what you want to learn:
- [ ] Basic API calls and responses
- [ ] Prompt engineering techniques
- [ ] Function calling capabilities
- [ ] System prompts and role definitions
- [ ] Multi-turn conversations
- [ ] Error handling and rate limiting
- [ ] Cost optimization strategies
- [ ] Integration patterns

Remember: This is about learning through experimentation. Don't aim for production-ready code - aim for understanding!