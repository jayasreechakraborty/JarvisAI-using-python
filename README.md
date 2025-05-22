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

Setup Instructions:

#Clone the Repository

-git clone https://github.com/yourusername/jarvis-ai.git
-cd jarvis-ai

#Install Required Python Libraries

-pip install -r requirements.txt

#If requirements.txt is not available, install manually:

-pip install speechrecognition pyttsx3 requests

-pip install pipwin

-pipwin install pyaudio

Note: pyaudio is required for microphone input and may need special installation on Windows.

#Setup Groq API

Go to https://console.groq.com and log in.

#Generate your Groq API Key.

-Replace the placeholder string "USE-YOUR-API-KEY-HERE" in both main.py and openaitest.py with your actual API key.

Running the Assistant

-python main.py

Jarvis will greet you and begin listening for your commands.

#Testing Groq API Separately

To verify your Groq API setup:

-python openaitest.py

You should get a joke or AI response from the llama3-70b-8192 model.

#Example Voice Commands

Command	Action:

-"Open YouTube"	Opens YouTube

-"Play music"	Plays the configured audio file

-"Open WhatsApp"	Launches WhatsApp via Windows shell

-"What is the time"	Speaks out the current time

-"Using artificial intelligence..."	Prompts for an AI-powered question

#Customization

-Change Music Path: Edit the musicPath variable in main.py.

-Modify App Launchers: Update the apps dictionary with the correct Windows App IDs for your system.

-Change Name/Greeting: Update "Hello rc" to your preferred name in say() functions.

#Requirements

-Windows OS (tested on Windows 10/11)

-Python 3.8 or newer

-Microphone for voice input

-Internet connection for Groq API

#Powered By:

-Groq AI (LLaMA 3)

-SpeechRecognition

-pyttsx3 TTS

-Python Requests

#License

This project is open-source and available for educational or personal use. Feel free to modify and build upon it.

#Author

Made with care by RC for learning and experimenting with AI.



