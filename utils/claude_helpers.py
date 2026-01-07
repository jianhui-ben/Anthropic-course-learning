"""
Helper functions for working with Claude API
Following the tutorial pattern for message management
"""
import os
from anthropic import Anthropic
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Global client instance
client = None

def get_claude_client():
    """Initialize and return Claude client"""
    global client
    if client is None:
        api_key = os.getenv('ANTHROPIC_API_KEY')
        if not api_key:
            raise ValueError("ANTHROPIC_API_KEY not found in environment variables")
        client = Anthropic(api_key=api_key)
    return client

def add_user_message(messages, text):
    """Add a user message to the messages list"""
    user_message = {"role": "user", "content": text}
    messages.append(user_message)

def add_assistant_message(messages, text):
    """Add an assistant message to the messages list"""
    assistant_message = {"role": "assistant", "content": text}
    messages.append(assistant_message)

def chat(messages, model="claude-3-haiku-20240307", max_tokens=1000):
    """
    Send messages to Claude and return response text
    
    Args:
        messages (list): List of message dictionaries
        model (str): Model to use
        max_tokens (int): Maximum tokens in response
    
    Returns:
        str: Claude's response text
    """
    client = get_claude_client()
    
    message = client.messages.create(
        model=model,
        max_tokens=max_tokens,
        messages=messages,
    )
    
    return message.content[0].text

def simple_chat(message, model="claude-3-haiku-20240307", max_tokens=1000):
    """
    Simple chat function for quick experiments
    
    Args:
        message (str): The message to send to Claude
        model (str): Model to use
        max_tokens (int): Maximum tokens in response
    
    Returns:
        str: Claude's response
    """
    messages = []
    add_user_message(messages, message)
    return chat(messages, model, max_tokens)

def print_response(response):
    """Pretty print Claude's response"""
    print("=" * 50)
    print("Claude's Response:")
    print("=" * 50)
    print(response)
    print("=" * 50)