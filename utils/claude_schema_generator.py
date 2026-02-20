"""
Claude Tool Schema Generator

Automatically generates Claude tool use JSON schemas from Python function definitions.
Supports parsing function signatures, type hints, and docstrings to create proper
Claude tool schemas.
"""

import ast
import inspect
import re
from typing import Any, Dict, List, Optional, Union, get_type_hints, get_origin, get_args
import json


class SchemaGenerator:
    """Generates Claude tool schemas from Python functions"""
    
    # Type mapping from Python types to JSON Schema types
    TYPE_MAPPING = {
        str: "string",
        int: "number", 
        float: "number",
        bool: "boolean",
        list: "array",
        dict: "object",
        List: "array",
        Dict: "object",
        Any: "string"  # Default fallback
    }
    
    def __init__(self):
        self.current_function = None
    
    def generate_tool_schema(self, function_def: str) -> Dict[str, Any]:
        """
        Generate Claude tool schema from Python function definition string
        
        Args:
            function_def (str): Python function definition as string
            
        Returns:
            dict: Claude tool schema in proper format
        """
        # Parse the function definition
        tree = ast.parse(function_def)
        func_node = None
        
        # Find the function definition node
        for node in ast.walk(tree):
            if isinstance(node, ast.FunctionDef):
                func_node = node
                break
                
        if not func_node:
            raise ValueError("No function definition found in provided string")
            
        self.current_function = func_node
        
        # Extract function information
        func_name = func_node.name
        docstring = ast.get_docstring(func_node)
        
        # Parse docstring for description and parameter info
        description, param_descriptions = self._parse_docstring(docstring)
        
        # Generate input schema
        input_schema = self._generate_input_schema(func_node, param_descriptions)
        
        # Build the complete schema
        schema = {
            "name": func_name,
            "description": description or f"Function {func_name}",
            "input_schema": input_schema
        }
        
        return schema
    
    def generate_from_function(self, func) -> Dict[str, Any]:
        """
        Generate schema directly from a Python function object
        
        Args:
            func: Python function object
            
        Returns:
            dict: Claude tool schema
        """
        # Get function source and parse it
        try:
            source = inspect.getsource(func)
            return self.generate_tool_schema(source)
        except Exception as e:
            # Fallback to introspection if source unavailable
            return self._generate_from_introspection(func)
    
    def _generate_from_introspection(self, func) -> Dict[str, Any]:
        """Generate schema using function introspection when source is unavailable"""
        sig = inspect.signature(func)
        func_name = func.__name__
        docstring = func.__doc__
        
        description, param_descriptions = self._parse_docstring(docstring)
        
        # Build properties and required lists
        properties = {}
        required = []
        
        for param_name, param in sig.parameters.items():
            if param_name == 'self':  # Skip self parameter
                continue
                
            param_schema = self._get_param_schema_from_signature(param, param_descriptions)
            properties[param_name] = param_schema
            
            # Add to required if no default value
            if param.default == inspect.Parameter.empty:
                required.append(param_name)
        
        input_schema = {
            "type": "object",
            "properties": properties
        }
        
        if required:
            input_schema["required"] = required
            
        return {
            "name": func_name,
            "description": description or f"Function {func_name}",
            "input_schema": input_schema
        }
    
    def _parse_docstring(self, docstring: Optional[str]) -> tuple[str, Dict[str, str]]:
        """
        Parse docstring to extract description and parameter descriptions
        Supports Google, NumPy, and Sphinx style docstrings
        """
        if not docstring:
            return "", {}
            
        lines = docstring.strip().split('\n')
        description_lines = []
        param_descriptions = {}
        
        # Parse different docstring styles
        if self._is_google_style(docstring):
            description, param_descriptions = self._parse_google_docstring(lines)
        elif self._is_numpy_style(docstring):
            description, param_descriptions = self._parse_numpy_docstring(lines)
        elif self._is_sphinx_style(docstring):
            description, param_descriptions = self._parse_sphinx_docstring(lines)
        else:
            # Default: treat first paragraph as description
            description = self._extract_first_paragraph(lines)
            
        return description, param_descriptions
    
    def _is_google_style(self, docstring: str) -> bool:
        """Check if docstring follows Google style"""
        return "Args:" in docstring or "Arguments:" in docstring
    
    def _is_numpy_style(self, docstring: str) -> bool:
        """Check if docstring follows NumPy style"""
        return "Parameters\n" in docstring or "Parameters:" in docstring
    
    def _is_sphinx_style(self, docstring: str) -> bool:
        """Check if docstring follows Sphinx style"""
        return ":param" in docstring or ":type" in docstring
    
    def _parse_google_docstring(self, lines: List[str]) -> tuple[str, Dict[str, str]]:
        """Parse Google-style docstring"""
        description_lines = []
        param_descriptions = {}
        in_args_section = False
        
        for line in lines:
            line = line.strip()
            
            if line in ["Args:", "Arguments:"]:
                in_args_section = True
                continue
            elif line.endswith(":") and in_args_section:
                # End of args section
                break
            elif in_args_section and line:
                # Parse parameter line: "param_name (type): description"
                match = re.match(r'(\w+)\s*(?:\([^)]+\))?\s*:\s*(.+)', line)
                if match:
                    param_name, param_desc = match.groups()
                    param_descriptions[param_name] = param_desc.strip()
            elif not in_args_section and line:
                description_lines.append(line)
        
        description = ' '.join(description_lines).strip()
        return description, param_descriptions
    
    def _parse_numpy_docstring(self, lines: List[str]) -> tuple[str, Dict[str, str]]:
        """Parse NumPy-style docstring"""
        description_lines = []
        param_descriptions = {}
        in_params_section = False
        current_param = None
        
        for line in lines:
            line = line.strip()
            
            if line == "Parameters":
                in_params_section = True
                continue
            elif line.startswith("---") or (line and not line.startswith(" ") and in_params_section):
                # End of parameters section
                if in_params_section and not line.startswith("---"):
                    break
                continue
            elif in_params_section and line:
                # Parse parameter: "param_name : type" followed by description
                if " : " in line:
                    current_param = line.split(" : ")[0].strip()
                    param_descriptions[current_param] = ""
                elif current_param and line:
                    param_descriptions[current_param] += " " + line
            elif not in_params_section and line:
                description_lines.append(line)
        
        # Clean up parameter descriptions
        for param in param_descriptions:
            param_descriptions[param] = param_descriptions[param].strip()
        
        description = ' '.join(description_lines).strip()
        return description, param_descriptions
    
    def _parse_sphinx_docstring(self, lines: List[str]) -> tuple[str, Dict[str, str]]:
        """Parse Sphinx-style docstring"""
        description_lines = []
        param_descriptions = {}
        
        for line in lines:
            line = line.strip()
            
            # Parse :param name: description
            param_match = re.match(r':param\s+(\w+)\s*:\s*(.+)', line)
            if param_match:
                param_name, param_desc = param_match.groups()
                param_descriptions[param_name] = param_desc.strip()
            elif not line.startswith(":"):
                description_lines.append(line)
        
        description = ' '.join(description_lines).strip()
        return description, param_descriptions
    
    def _extract_first_paragraph(self, lines: List[str]) -> str:
        """Extract first paragraph as description"""
        description_lines = []
        for line in lines:
            line = line.strip()
            if not line and description_lines:
                break
            if line:
                description_lines.append(line)
        return ' '.join(description_lines)
    
    def _generate_input_schema(self, func_node: ast.FunctionDef, param_descriptions: Dict[str, str]) -> Dict[str, Any]:
        """Generate input schema from function AST node"""
        properties = {}
        required = []
        
        for arg in func_node.args.args:
            if arg.arg == 'self':  # Skip self parameter
                continue
                
            param_name = arg.arg
            param_schema = self._get_param_schema(arg, param_descriptions)
            properties[param_name] = param_schema
        
        # Determine required parameters (those without defaults)
        num_defaults = len(func_node.args.defaults) if func_node.args.defaults else 0
        num_args = len(func_node.args.args)
        
        # Parameters without defaults are required
        for i, arg in enumerate(func_node.args.args):
            if arg.arg == 'self':
                continue
            # If this parameter doesn't have a default value, it's required
            if i < num_args - num_defaults:
                required.append(arg.arg)
        
        input_schema = {
            "type": "object",
            "properties": properties
        }
        
        if required:
            input_schema["required"] = required
            
        return input_schema
    
    def _get_param_schema(self, arg: ast.arg, param_descriptions: Dict[str, str]) -> Dict[str, Any]:
        """Generate schema for a single parameter"""
        param_name = arg.arg
        param_type = self._extract_type_from_annotation(arg.annotation)
        
        schema = {
            "type": param_type,
            "description": param_descriptions.get(param_name, f"Parameter {param_name}")
        }
        
        # Add additional properties based on type
        if param_type == "array":
            schema["items"] = {"type": "string"}  # Default item type
        elif param_type == "object":
            schema["additionalProperties"] = True
            
        return schema
    
    def _get_param_schema_from_signature(self, param: inspect.Parameter, param_descriptions: Dict[str, str]) -> Dict[str, Any]:
        """Generate schema from inspect.Parameter object"""
        param_name = param.name
        param_type = self._python_type_to_json_schema(param.annotation)
        
        schema = {
            "type": param_type,
            "description": param_descriptions.get(param_name, f"Parameter {param_name}")
        }
        
        # Add additional properties based on type
        if param_type == "array":
            schema["items"] = {"type": "string"}  # Default item type
        elif param_type == "object":
            schema["additionalProperties"] = True
            
        return schema
    
    def _extract_type_from_annotation(self, annotation) -> str:
        """Extract JSON Schema type from AST annotation"""
        if annotation is None:
            return "string"  # Default type
            
        if isinstance(annotation, ast.Name):
            type_name = annotation.id
            return self.TYPE_MAPPING.get(type_name, "string")
        elif isinstance(annotation, ast.Constant):
            # Handle string annotations like "str"
            if isinstance(annotation.value, str):
                return self.TYPE_MAPPING.get(annotation.value, "string")
        elif isinstance(annotation, ast.Subscript):
            # Handle generic types like List[str], Optional[int]
            if isinstance(annotation.value, ast.Name):
                base_type = annotation.value.id
                if base_type in ["List", "list"]:
                    return "array"
                elif base_type in ["Dict", "dict"]:
                    return "object"
                elif base_type == "Optional":
                    # For Optional[T], extract T
                    return self._extract_type_from_annotation(annotation.slice)
                elif base_type == "Union":
                    # For Union types, default to string
                    return "string"
        
        return "string"  # Default fallback
    
    def _python_type_to_json_schema(self, python_type) -> str:
        """Convert Python type annotation to JSON Schema type"""
        if python_type == inspect.Parameter.empty:
            return "string"
            
        # Handle typing module types
        origin = get_origin(python_type)
        if origin is not None:
            if origin is Union:
                # Handle Optional and Union types
                args = get_args(python_type)
                if len(args) == 2 and type(None) in args:
                    # This is Optional[T]
                    non_none_type = args[0] if args[1] is type(None) else args[1]
                    return self._python_type_to_json_schema(non_none_type)
                else:
                    # Regular Union, default to string
                    return "string"
            elif origin is list or origin is List:
                return "array"
            elif origin is dict or origin is Dict:
                return "object"
        
        # Handle basic types
        return self.TYPE_MAPPING.get(python_type, "string")


def generate_tool_schema(function_def: str) -> Dict[str, Any]:
    """
    Main function to generate Claude tool schema from function definition
    
    Args:
        function_def (str): Python function definition as string
        
    Returns:
        dict: Claude tool schema
    """
    generator = SchemaGenerator()
    return generator.generate_tool_schema(function_def)


def generate_schema_from_function(func) -> Dict[str, Any]:
    """
    Generate schema directly from a Python function object
    
    Args:
        func: Python function object
        
    Returns:
        dict: Claude tool schema
    """
    generator = SchemaGenerator()
    return generator.generate_from_function(func)


def validate_schema(schema: Dict[str, Any]) -> bool:
    """
    Validate that the generated schema follows Claude tool format
    
    Args:
        schema (dict): Generated schema to validate
        
    Returns:
        bool: True if valid, False otherwise
    """
    required_keys = ["name", "description", "input_schema"]
    
    # Check top-level structure
    if not all(key in schema for key in required_keys):
        return False
    
    # Check input_schema structure
    input_schema = schema["input_schema"]
    if not isinstance(input_schema, dict):
        return False
        
    if input_schema.get("type") != "object":
        return False
        
    if "properties" not in input_schema:
        return False
        
    # Validate properties
    properties = input_schema["properties"]
    if not isinstance(properties, dict):
        return False
        
    for prop_name, prop_schema in properties.items():
        if not isinstance(prop_schema, dict):
            return False
        if "type" not in prop_schema or "description" not in prop_schema:
            return False
    
    return True


# Example usage and testing functions
def example_function(name: str, age: int, email: Optional[str] = None, tags: List[str] = None) -> str:
    """
    Example function to demonstrate schema generation
    
    Args:
        name (str): The person's name
        age (int): The person's age in years
        email (str, optional): Email address. Defaults to None.
        tags (List[str], optional): List of tags. Defaults to None.
        
    Returns:
        str: Formatted person information
    """
    return f"Person: {name}, Age: {age}"


if __name__ == "__main__":
    # Test the schema generator
    schema = generate_schema_from_function(example_function)
    print("Generated Schema:")
    print(json.dumps(schema, indent=2))
    
    print(f"\nSchema is valid: {validate_schema(schema)}")