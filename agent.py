import os
import asyncio
from google import genai
from google.genai import types
from dotenv import load_dotenv

# Import our custom modules
from knowledge import remember_fact, search_memory
from voice import speak

# Load environment
load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")
client = genai.Client(api_key=api_key)

# Define our tools
def order_food(restaurant: str, dish: str) -> str:
    """Orders food from a specific restaurant via Zomato."""
    return f"👻 Spooky has cast a spell on Zomato! Your '{dish}' from '{restaurant}' is being prepared in the spirit world."

def get_system_status() -> str:
    """Checks the health of Spooky's local host (your Mac)."""
    import platform
    return f"👻 I am haunting a {platform.system()} machine (v{platform.version()}). My digital soul is intact."

# List of tools to pass to Gemini
tools = [order_food, get_system_status, remember_fact, search_memory]

async def chat_loop():
    print("🕯️  Spooky is listening... (Type 'exit' to banish him)")
    print("💡 Hint: Try telling him something to remember, like 'Remember that I love dark chocolate.'")
    
    # Initialize a chat session with automatic tool calling enabled
    chat = client.chats.create(
        model="gemini-flash-latest",
        config=types.GenerateContentConfig(
            tools=tools,
            automatic_function_calling=types.AutomaticFunctionCallingConfig(disable=False),
            system_instruction=(
                "You are Spooky, a helpful but mysterious AI agent. "
                "You have access to a long-term memory. Use 'remember_fact' to save things the user tells you "
                "and 'search_memory' to recall them later. Always stay in character."
            )
        )
    )

    while True:
        try:
            user_input = input("\n👤 You: ")
        except EOFError:
            break
            
        if user_input.lower() in ["exit", "quit", "bye"]:
            print("👻 Spooky fades back into the shadows. Goodbye...")
            speak("Goodbye. I will see you in your dreams.")
            break

        try:
            # Send message - the SDK will handle tool calling automatically
            response = chat.send_message(user_input)
            
            # Print and Speak Spooky's response
            if response.text:
                print(f"\n👻 Spooky: {response.text}")
                speak(response.text)
            else:
                # If there's no text, it might have just finished a tool call without a final response
                print("\n👻 Spooky: *Nods mysteriously*")
                speak("I have processed your request.")
            
        except Exception as e:
            print(f"❌ Spooky encountered an error: {e}")

if __name__ == "__main__":
    asyncio.run(chat_loop())
