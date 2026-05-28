# Project Spooky: Local AI Agent

## 👻 Project Overview
Spooky is a local AI agent designed to be a personal assistant with a "soul." It uses the Gemini LLM as its brain and is capable of performing tasks on the user's behalf through MCP (Model Context Protocol).

## 🎯 Core Features
- **Brain:** Gemini 1.5/2.0 Integration via Python SDK.
- **Action Layer:** Support for MCP servers to interact with local tools, web services (e.g., Zomato), and system commands.
- **Memory/Knowledge:** Future integration of local knowledge bases (RAG) for personal context.
- **Speech:** Voice interaction (Speech-to-Text and Text-to-Speech).
- **Aesthetics:** A "Ultron-like" animated UI for visual presence.

## 🏗️ Technical Architecture (Proposed)
- **Language:** Python 3.14 (Backend & AI Logic).
- **Framework:** FastAPI (for API communication between UI and Agent).
- **MCP:** `mcp` Python library for tool orchestration.
- **UI:** Web-based interface (HTML/CSS/JS) using Three.js or stylized CSS for the "Ultron" pulse animation.
- **Speech:** 
    - STT: Faster-Whisper or Google Speech-to-Text.
    - TTS: Pyttsx3 (basic) or ElevenLabs/Bark (high-quality).

## 🗺️ Roadmap
### Phase 1: Foundation
- [x] Set up Python virtual environment.
- [x] Implement basic Gemini Chat loop in Python.
- [x] Integrate basic MCP client / Tool calling.
- [x] **Creative Skills:** Storytelling, spooky jokes, and persona-driven interaction.

### Phase 2: Action & Knowledge
- [x] Implement long-term memory (ChromaDB).

### Phase 3: Senses & Presence
- [ ] Integrate STT/TTS for voice control.
- [ ] Build the web-based animated UI.

## 📝 Notes
- Workspace: `~/spooky-agent`
- Primary Language: Python
