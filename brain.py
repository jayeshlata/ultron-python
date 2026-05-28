import os
from google import genai
from dotenv import load_dotenv

# Load environment variables
load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    print("❌ Error: GEMINI_API_KEY not found in .env file.")
    exit(1)

# Initialize the modern Gemini Client
client = genai.Client(api_key=api_key)

def test_brain():
    try:
        print("🕯️  Re-awakening Spooky's brain with the modern SDK...")
        
        # Using the latest flash model
        response = client.models.generate_content(
            model="gemini-flash-latest",
            contents="Introduce yourself in one spooky sentence as an AI agent named Spooky."
        )
        
        print(f"\n👻 Spooky says: {response.text}")
        print("\n✅ Brain is online and connected using the latest google-genai SDK!")
        
    except Exception as e:
        print(f"❌ Connection failed: {e}")

if __name__ == "__main__":
    test_brain()
