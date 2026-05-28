tell application "Terminal"
    do script "bash /Users/jayesh/workspace/spooky-agent/launch_spooky.sh"
    activate
end tell
delay 3
tell application "Safari"
    open location "http://localhost:8000"
    activate
end tell
