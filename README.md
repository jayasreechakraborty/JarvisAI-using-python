# Jarvis AI – Voice Assistant Using GROQ (LLaMA 3)

Jarvis is a voice-activated desktop AI assistant built in Python.
It listens to your voice commands, opens websites and applications, plays music, tells the time, and even answers your questions using **LLama 3 via GROQ API**.

##  Features

- Voice command recognition (using your microphone)
- Opens popular websites like YouTube, Google, Wikipedia
- Plays music from a local file
- Tells the current time
- Answers any question using **LLama 3 (70B)** via **GROQ Cloud API**
- Opens desktop apps like WhatsApp, Netflix, Spotify (customizable)
- Speaks responses using text-to-speech

Jarvis-AI/

├── main.py # Main voice assistant script

├── openaitest.py # Script to test the Groq API response

└── README.md # Project documentation

## Tech Stack

| Component | Purpose |
|----------|---------|
| `speech_recognition` | Capture voice input |
| `pyttsx3` | Text-to-speech (offline) |
| `requests` | Call GROQ API for AI answers |
| `webbrowser` & `os` | Open websites & local apps |
| `datetime` | Time-related features |
| `Python` | Core programming language |


1. Clone the Repository

```bash
git clone https://github.com/yourusername/jarvis-ai-groq.git
cd jarvis-ai-groq   


