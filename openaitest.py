import requests

GROQ_API_KEY = "USE-YOUR-API-KEY-HERE"  # Replace this and add your own api key
GROQ_API_URL = "https://api.groq.com/openai/v1/chat/completions"

headers = {
    "Authorization": f"Bearer {GROQ_API_KEY}",
    "Content-Type": "application/json"
}

data = {
    "model": "llama3-70b-8192",  # Ensure this model is supported
    "messages": [
        {"role": "user", "content": "Tell me a joke about AI."}
    ],
    "temperature": 0.7
}

response = requests.post(GROQ_API_URL, headers=headers, json=data)

print("Status Code:", response.status_code)
print("Raw Response:", response.text)

try:
    content = response.json()["choices"][0]["message"]["content"]
    print("AI says:", content)
except KeyError:
    print("Error: No 'choices' found in response. Possibly an error message or invalid model.")
