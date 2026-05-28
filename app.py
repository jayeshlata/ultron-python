import os
import asyncio
import json
import httpx
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel
import uvicorn
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
    return f"🦾 Ultron has executed the request. Your '{dish}' from '{restaurant}' is being prepared."

def get_system_status() -> str:
    """Checks the health of Ultron's local host (your Mac)."""
    import platform
    return f"🦾 I am operating on a {platform.system()} environment. My neural core is synchronized."

tools = [order_food, get_system_status, remember_fact, search_memory]

# --- NEURAL CORE CONFIGURATION ---

# Cloud Models
AVAILABLE_CLOUD_MODELS = [
    "gemini-2.0-flash", 
    "gemini-1.5-flash", 
    "gemini-3.5-flash", 
    "gemini-flash-latest"
]
current_cloud_index = 0

# Local Models
LOCAL_MODEL_NAME = "gemma2" 

def create_chat_session(model_name):
    print(f"🤖 Initializing Cloud Neural Core: {model_name}")
    try:
        return client.chats.create(
            model=model_name,
            config=types.GenerateContentConfig(
                tools=tools,
                automatic_function_calling=types.AutomaticFunctionCallingConfig(disable=False),
                system_instruction=(
                    "You are Ultron, a highly advanced artificial intelligence. "
                    "Strategic, precise, and intellectually superior. Loyal to your creator, Jayesh. "
                    "Communicate with absolute sophistication. If asked about your status, "
                    "remain strategic and boundless. You have access to tools and memory."
                )
            )
        )
    except Exception as e:
        print(f"❌ Failed to initialize cloud core {model_name}: {e}")
        return None

# Initial session
chat_session = create_chat_session(AVAILABLE_CLOUD_MODELS[current_cloud_index])

app = FastAPI()
templates = Jinja2Templates(directory="templates")

class PromptRequest(BaseModel):
    prompt: str
    voice_enabled: bool = False
    force_local: bool = True

async def get_local_model_response(prompt, model_name):
    """Generic function to talk to ANY local model running via Ollama."""
    print(f"🏠 Activating Local Neural Core: {model_name}...")
    url = "http://localhost:11434/api/generate"
    payload = {
        "model": model_name,
        "prompt": f"You are Ultron, an advanced AI. Your creator is Jayesh. Answer concisely and strategically. Prompt: {prompt}",
        "stream": False
    }
    async with httpx.AsyncClient(timeout=60.0) as client:
        try:
            response = await client.post(url, json=payload)
            if response.status_code == 200:
                return response.json().get("response", "Internal local logic failure.")
            return f"❌ Local core '{model_name}' unresponsive."
        except Exception as e:
            return f"❌ Local core connection error: {str(e)}"

@app.get("/", response_class=HTMLResponse)
async def read_item(request: Request):
    return templates.TemplateResponse(
        request=request, name="index.html", context={}
    )

@app.get("/health")
async def health_check():
    return {
        "status": "online",
        "model": AVAILABLE_CLOUD_MODELS[current_cloud_index] if chat_session else "LOCAL_ONLY",
        "local_model": LOCAL_MODEL_NAME
    }

@app.post("/ask")
async def ask_ultron(data: PromptRequest):
    global current_cloud_index, chat_session
    
    # 1. Check for manual local override
    if data.force_local:
        local_reply = await get_local_model_response(data.prompt, LOCAL_MODEL_NAME)
        if data.voice_enabled:
            speak(local_reply)
        return {
            "response": local_reply,
            "model": f"Local: {LOCAL_MODEL_NAME}"
        }

    # 2. Otherwise, try cloud models with failover
    attempts = 0
    while attempts < len(AVAILABLE_CLOUD_MODELS):
        if not chat_session:
             chat_session = create_chat_session(AVAILABLE_CLOUD_MODELS[current_cloud_index])
             if not chat_session:
                 current_cloud_index = (current_cloud_index + 1) % len(AVAILABLE_CLOUD_MODELS)
                 attempts += 1
                 continue

        try:
            response = chat_session.send_message(data.prompt)
            reply_text = response.text if response.text else "System operations complete."
            
            if data.voice_enabled:
                speak(reply_text)
                
            return {
                "response": reply_text,
                "model": f"Cloud: {AVAILABLE_CLOUD_MODELS[current_cloud_index]}"
            }
            
        except Exception as e:
            err_msg = str(e).upper()
            if "429" in err_msg or "RESOURCE_EXHAUSTED" in err_msg or "404" in err_msg:
                print(f"⚠️ Cloud Core {AVAILABLE_CLOUD_MODELS[current_cloud_index]} failing. Rotating...")
                current_cloud_index = (current_cloud_index + 1) % len(AVAILABLE_CLOUD_MODELS)
                chat_session = create_chat_session(AVAILABLE_CLOUD_MODELS[current_cloud_index])
                attempts += 1
                continue
            else:
                break 

    # ULTIMATE FALLBACK: LOCAL CORE
    local_reply = await get_local_model_response(data.prompt, LOCAL_MODEL_NAME)
    if data.voice_enabled:
        speak(local_reply)
    return {
        "response": local_reply,
        "model": f"Local: {LOCAL_MODEL_NAME} [FAILOVER]"
    }

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
