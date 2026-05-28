#!/bin/bash
# Spooky Launcher Script - Web Integrated Version

# 1. Navigate to the project directory
cd "/Users/jayesh/workspace/spooky-agent"

# 2. Kill any existing instances on port 8000
lsof -ti:8000 | xargs kill -9 2>/dev/null || true

# 3. Start the Web-Integrated Spooky Server
echo "👻 Awakening Spooky in the Web Realm..."
./venv/bin/python3 app.py
