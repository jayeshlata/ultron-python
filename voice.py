import subprocess

def speak(text: str):
    """Uses the native macOS 'say' command to speak text with an Indian male accent."""
    try:
        # Clean text of emojis and common AI markers for cleaner speech
        clean_text = text.replace("👻", "").replace("👤", "").replace("🕯️", "").replace("💡", "")
        clean_text = clean_text.replace("*", "").replace("#", "")
        
        # 'Rishi' is the high-quality Indian English male voice on macOS.
        # It is stable, clear, and fits the advanced AI persona.
        subprocess.run(["say", "-v", "Rishi", clean_text])
    except Exception as e:
        print(f"Error in speech: {e}")

if __name__ == "__main__":
    speak("I am Spooky. My neural systems are fully operational, Jayesh.")
