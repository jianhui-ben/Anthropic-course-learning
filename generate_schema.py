#!/usr/bin/env python3
"""
CLI script for generating Claude tool schemas from Python functions

Usage:
    python generate_schema.py <python_file> <function_name>
    python generate_schema.py --help
    
Examples:
    python generate_schema.py utils/claude_helpers.py simple_chat
    python generate_schema.py my_functions.py calculate_area
"""

import argparse
import importlib.util
import inspect
import json
import sys
from pathlib import Path

# Add utils to path so we can import our schema generator
sys.path.insert(0, str(Path(__file__).parent / "utils"))

from claude_schema_generator import generate_schema_from_function, validate_schema


def load_function_from_file(file_path: str, function_name: str):
    """
    Load a specific function from a Python file
    
    Args:
        file_path (str): Path to the Python file
        function_name (str): Name of the function to load
        
    Returns:
        function: The loaded function object
    """
    # Convert to Path object for easier handling
    file_path = Path(file_path)
    
    if not file_path.exists():
        raise FileNotFoundError(f"File not found: {file_path}")
    
    if not file_path.suffix == '.py':
        raise ValueError(f"File must be a Python file (.py): {file_path}")
    
    # Load the module
    spec = importlib.util.spec_from_file_location("temp_module", file_path)
    if spec is None or spec.loader is None:
        raise ImportError(f"Could not load module from {file_path}")
    
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    
    # Get the function
    if not hasattr(module, function_name):
        available_functions = [name for name in dir(module) 
                             if callable(getattr(module, name)) and not name.startswith('_')]
        raise AttributeError(
            f"Function '{function_name}' not found in {file_path}. "
            f"Available functions: {', '.join(available_functions)}"
        )
    
    return getattr(module, function_name)


def list_functions_in_file(file_path: str) -> list:
    """
    List all functions in a Python file
    
    Args:
        file_path (str): Path to the Python file
        
    Returns:
        list: List of function names
    """
    file_path = Path(file_path)
    
    if not file_path.exists():
        raise FileNotFoundError(f"File not found: {file_path}")
    
    # Load the module
    spec = importlib.util.spec_from_file_location("temp_module", file_path)
    if spec is None or spec.loader is None:
        raise ImportError(f"Could not load module from {file_path}")
    
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    
    # Get all functions
    functions = []
    for name in dir(module):
        obj = getattr(module, name)
        if callable(obj) and not name.startswith('_') and inspect.isfunction(obj):
            functions.append(name)
    
    return functions


def main():
    parser = argparse.ArgumentParser(
        description="Generate Claude tool schemas from Python functions",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  %(prog)s utils/claude_helpers.py simple_chat
  %(prog)s my_functions.py calculate_area --output schema.json
  %(prog)s utils/claude_helpers.py --list
        """
    )
    
    parser.add_argument(
        "file_path",
        help="Path to the Python file containing the function"
    )
    
    parser.add_argument(
        "function_name",
        nargs="?",
        help="Name of the function to generate schema for"
    )
    
    parser.add_argument(
        "--list", "-l",
        action="store_true",
        help="List all functions in the file instead of generating schema"
    )
    
    parser.add_argument(
        "--output", "-o",
        help="Output file path (default: print to stdout)"
    )
    
    parser.add_argument(
        "--validate", "-v",
        action="store_true",
        help="Validate the generated schema"
    )
    
    parser.add_argument(
        "--pretty", "-p",
        action="store_true",
        default=True,
        help="Pretty print JSON output (default: True)"
    )
    
    args = parser.parse_args()
    
    try:
        # List functions mode
        if args.list:
            functions = list_functions_in_file(args.file_path)
            print(f"Functions in {args.file_path}:")
            for func_name in functions:
                print(f"  - {func_name}")
            return
        
        # Generate schema mode
        if not args.function_name:
            parser.error("function_name is required unless using --list")
        
        # Load the function
        func = load_function_from_file(args.file_path, args.function_name)
        
        # Generate schema
        print(f"Generating schema for {args.function_name}...", file=sys.stderr)
        schema = generate_schema_from_function(func)
        
        # Validate if requested
        if args.validate:
            is_valid = validate_schema(schema)
            print(f"Schema validation: {'PASSED' if is_valid else 'FAILED'}", file=sys.stderr)
            if not is_valid:
                sys.exit(1)
        
        # Format output
        if args.pretty:
            output = json.dumps(schema, indent=2, ensure_ascii=False)
        else:
            output = json.dumps(schema, ensure_ascii=False)
        
        # Write output
        if args.output:
            with open(args.output, 'w', encoding='utf-8') as f:
                f.write(output)
            print(f"Schema written to {args.output}", file=sys.stderr)
        else:
            print(output)
            
    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()