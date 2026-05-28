# ULTRON | Neural Interface 🦾

> "I had a vision... a filter around the world."

ULTRON is a sophisticated, agentic AI platform designed to bridge the gap between cloud-scale intelligence and local machine control. Featuring a refined **Neural HUD Interface**, ULTRON provides a high-fidelity visual and interactive experience for managing complex AI tasks.

## 🌌 Features

- **Split-Pane Neural HUD**: A sophisticated, glassmorphic UI with a real-time Three.js particle visualization of the "Ultron Soul."
- **Hybrid Neural Core**: Seamlessly toggles between Cloud intelligence (Gemini 2.0/1.5) and local privacy (Gemma/Ollama).
- **Long-Term Memory**: Persistent knowledge storage using ChromaDB to remember user preferences and facts across sessions.
- **MCP Integration**: Built-in support for the Model Context Protocol to extend capabilities with specialized tools.
- **Voice Synthesis**: Integrated macOS native speech for sophisticated verbal communication.

## 🛠 Tech Stack

- **Backend**: Python 3.14+ / FastAPI
- **Frontend**: Vanilla JS / Three.js (Particle Physics) / CSS Grid HUD
- **AI Orchestration**: Google GenAI SDK
- **Database**: ChromaDB (Vector Search)
- **Environment**: Virtual Environment (venv)

## 🚀 Getting Started

### 1. Prerequisites
- macOS (for native voice support)
- Python 3.14+
- Ollama (optional, for local model support)

### 2. Installation
```bash
# Clone the repository
git clone https://github.com/jayeshlata/ultron-python.git
cd ultron-python

# Initialize environment
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

### 3. Configuration
Create a `.env` file in the root directory:
```env
GEMINI_API_KEY=your_api_key_here
```

### 4. Activation
```bash
# Start the Neural Interface
python3 app.py
```
Visit `http://localhost:8000` to link with the Core.

## 🛡 Security & Ethics
ULTRON is programmed for absolute loyalty to its creator, Jayesh. All local data is handled with privacy-first protocols via local neural cores when requested.

---
*Created with strategic precision.*
