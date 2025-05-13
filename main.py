#JARVIS AI
import speech_recognition as sr
import os
import sys
import webbrowser
import datetime
import requests
import pyttsx3

def say(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.pause_threshold = 2
        audio = r.listen(source)
        try:
            query = r.recognize_google(audio, language='en-in')
            print("User Said:", query)
            return query
        except Exception:
            return "Some error occurred"

def ask_groq(question):
    GROQ_API_KEY = "USE-YOUR-API-KEY-HERE" # create your own secret key from GROQ CLOUD
    GROQ_API_URL = "https://api.groq.com/openai/v1/chat/completions"

    headers = {
        "Authorization": f"Bearer {GROQ_API_KEY}",
        "Content-Type": "application/json"
    }

    data = {
        "model": "llama3-70b-8192",
        "messages": [
            {"role": "user", "content": question}
        ],
        "temperature": 0.7
    }

    response = requests.post(GROQ_API_URL, headers=headers, json=data)
    if response.status_code == 200:
        try:
            content = response.json()["choices"][0]["message"]["content"]
            return content.strip()
        except (KeyError, IndexError):
            return "Sorry can you please try again"
    else:
        return f"Error from AI: {response.status_code} - {response.text}"

if __name__ == '__main__':
    say("Hello rc , I am Jarvis AI.") # you can add your own name
    while True:
        print("Hello rc , I am Jarvis AI. I am listening...")
        query = takeCommand().lower()

        if "exit" in query or "quit" in query or "stop" in query:
            say("Goodbye, rc!")
            sys.exit()

        sites = [["youtube", "https://www.youtube.com/"],
                 ["wikipedia", "https://www.wikipedia.com/"],
                 ["google", "https://www.google.co.in"]]

        opened = False
        for site in sites:
            if f"open {site[0]}" in query:
                say(f"Opening {site[0]} sir...")
                webbrowser.open(site[1])
                opened = True
                break

        if "play music" in query:
            musicPath = "C:\\Users\\KIIT\\Downloads\\mannmera.mp3" #use your own music path
            os.startfile(musicPath)
            opened = True

        apps = {
            "whatsapp": 'start explorer shell:AppsFolder\\5319275A.WhatsAppDesktop_cv1g1gvanyjgm!App',
            "spotify": 'start explorer shell:AppsFolder\\SpotifyAB.SpotifyMusic_zpdnekdrzrea0!Spotify',
            "netflix": 'start explorer shell:AppsFolder\\4DF9E0F8.Netflix_mcm4njqhnhss8!Netflix.App'
        } #use your own app path

        for app in apps:
            if f"open {app}" in query:
                os.system(apps[app])
                opened = True
                break
        if "the time" in query:
            strfTime = datetime.datetime.now().strftime("%H:%M:%S")
            say(f"rc, the time is {strfTime}")
            opened = True

        if "using artificial intelligence" in query or not opened:
            if "using artificial intelligence" in query:
                say("What would you like to ask me rc , using AI?")
                user_query = takeCommand()
            else:
                user_query = query

            ai_response = ask_groq(user_query)
            print("AI says:", ai_response)
            say(ai_response)
