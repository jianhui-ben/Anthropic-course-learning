# Claude Tool Schema Generator

A Python utility that automatically generates Claude tool use JSON schemas from Python function definitions. This makes it dead simple to convert any Python function into a proper Claude tool schema.

## Features

- **Automatic schema generation** from Python functions
- **Multiple docstring format support** (Google, NumPy, Sphinx styles)
- **Type hint parsing** with proper JSON Schema type mapping
- **CLI interface** for easy integration into workflows
- **Schema validation** to ensure Claude compatibility
- **Flexible usage** - from function objects or definition strings

## Quick Start

### 1. Generate Schema from Function

```python
from utils.claude_schema_generator import generate_schema_from_function

def get_weather(location: str, units: str = "celsius") -> dict:
    """
    Get weather information for a location
    
    Args:
        location (str): The city name
        units (str): Temperature units (celsius/fahrenheit)
    """
    return {"temp": 22, "condition": "sunny"}

schema = generate_schema_from_function(get_weather)
print(json.dumps(schema, indent=2))
```

### 2. Use CLI Script

```bash
# List all functions in a file
python generate_schema.py examples/sample_tools.py --list

# Generate schema for specific function
python generate_schema.py examples/sample_tools.py get_weather

# Generate with validation
python generate_schema.py examples/sample_tools.py get_weather --validate

# Save to file
python generate_schema.py examples/sample_tools.py get_weather --output weather_schema.json
```

## Generated Schema Format

The utility generates schemas in Claude's expected format:

```json
{
  "name": "get_weather",
  "description": "Get weather information for a location",
  "input_schema": {
    "type": "object",
    "properties": {
      "location": {
        "type": "string",
        "description": "The city name"
      },
      "units": {
        "type": "string", 
        "description": "Temperature units (celsius/fahrenheit)"
      }
    },
    "required": ["location"]
  }
}
```

## Supported Features

### Type Mapping
- `str` → `"string"`
- `int`, `float` → `"number"`
- `bool` → `"boolean"`
- `list`, `List[T]` → `"array"`
- `dict`, `Dict[K,V]` → `"object"`
- `Optional[T]` → Same as `T` (not required)
- `Union[T1, T2]` → `"string"` (fallback)

### Docstring Styles

**Google Style:**
```python
def func(param1: str, param2: int = 10):
    """
    Function description
    
    Args:
        param1 (str): Parameter description
        param2 (int): Another parameter
    """
```

**NumPy Style:**
```python
def func(param1: str, param2: int = 10):
    """
    Function description
    
    Parameters
    ----------
    param1 : str
        Parameter description
    param2 : int
        Another parameter
    """
```

**Sphinx Style:**
```python
def func(param1: str, param2: int = 10):
    """
    Function description
    
    :param param1: Parameter description
    :param param2: Another parameter
    """
```

## Files

- `utils/claude_schema_generator.py` - Main utility module
- `generate_schema.py` - CLI script
- `notebooks/08_schema_generator.ipynb` - Interactive examples
- `examples/sample_tools.py` - Sample functions for testing

## Usage Examples

See `notebooks/08_schema_generator.ipynb` for comprehensive examples including:
- Simple functions with type hints
- Complex functions with Optional and List parameters
- Different docstring styles
- Schema validation
- CLI usage demonstrations

## CLI Options

```
python generate_schema.py <file_path> [function_name] [options]

Options:
  --list, -l          List all functions in the file
  --output, -o FILE   Save schema to file
  --validate, -v      Validate generated schema
  --pretty, -p        Pretty print JSON (default: True)
  --help             Show help message
```

This utility follows the workspace philosophy of rapid prototyping and learning-first approach, making it easy to experiment with Claude tool creation!