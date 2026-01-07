"""
Interactive Multi-Turn Chatbot Example

This example shows how to create an interactive chatbot that maintains
conversation history using the input() function for user interaction.
"""

import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from utils.claude_helpers import add_user_message, add_assistant_message, chat, get_claude_client

def interactive_chatbot():
    """
    Run an interactive chatbot session with Claude
    """
    print("🤖 Claude Chatbot")
    print("=" * 40)
    print("Type 'quit', 'exit', or 'bye' to end the conversation")
    print("Type 'history' to see conversation history")
    print("Type 'clear' to start a new conversation")
    print("=" * 40)
    
    # Initialize conversation
    messages = []
    
    # Test connection first
    try:
        client = get_claude_client()
        print("✅ Connected to Claude API")
    except Exception as e:
        print(f"❌ Error connecting to Claude: {e}")
        return
    
    print("\nClaude: Hello! I'm Claude, an AI assistant. How can I help you today?")
    
    while True:
        try:
            # Get user input
            user_input = input("\nYou: ").strip()
            
            # Check for special commands
            if user_input.lower() in ['quit', 'exit', 'bye']:
                print("\nClaude: Goodbye! It was nice chatting with you.")
                break
            
            elif user_input.lower() == 'history':
                print(f"\n📊 Conversation History ({len(messages)} messages):")
                for i, msg in enumerate(messages, 1):
                    role = "You" if msg['role'] == 'user' else "Claude"
                    content = msg['content'][:100] + "..." if len(msg['content']) > 100 else msg['content']
                    print(f"{i}. {role}: {content}")
                continue
            
            elif user_input.lower() == 'clear':
                messages = []
                print("\n🔄 Conversation cleared. Starting fresh!")
                print("Claude: Hello again! How can I help you?")
                continue
            
            elif not user_input:
                print("Please enter a message or type 'quit' to exit.")
                continue
            
            # Add user message to conversation
            add_user_message(messages, user_input)
            
            # Get Claude's response
            print("\nClaude: ", end="", flush=True)
            try:
                response = chat(messages, max_tokens=500)
                print(response)
                
                # Add Claude's response to conversation history
                add_assistant_message(messages, response)
                
            except Exception as e:
                print(f"Sorry, I encountered an error: {e}")
                # Remove the user message if Claude couldn't respond
                messages.pop()
        
        except KeyboardInterrupt:
            print("\n\nClaude: Goodbye! (Interrupted by user)")
            break
        except EOFError:
            print("\n\nClaude: Goodbye!")
            break

def demo_conversation():
    """
    Demo function showing a pre-scripted conversation
    """
    print("🎭 Demo Conversation")
    print("=" * 40)
    
    messages = []
    demo_inputs = [
        "Hi! What's the weather like?",
        "I meant can you tell me about weather in general?",
        "What factors affect weather patterns?",
        "That's interesting! Can you explain how temperature affects weather?"
    ]
    
    try:
        for user_msg in demo_inputs:
            print(f"\nUser: {user_msg}")
            add_user_message(messages, user_msg)
            
            response = chat(messages, max_tokens=300)
            print(f"Claude: {response}")
            add_assistant_message(messages, response)
            
            # Small pause for readability
            input("\nPress Enter to continue...")
        
        print(f"\n📊 Final conversation had {len(messages)} messages")
        
    except Exception as e:
        print(f"Demo error: {e}")

if __name__ == "__main__":
    print("Choose an option:")
    print("1. Interactive chatbot")
    print("2. Demo conversation")
    
    choice = input("Enter choice (1 or 2): ").strip()
    
    if choice == "1":
        interactive_chatbot()
    elif choice == "2":
        demo_conversation()
    else:
        print("Invalid choice. Running interactive chatbot...")
        interactive_chatbot()