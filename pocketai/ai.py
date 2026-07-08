from config import config
import requests 

url = config["url"]
model = config["model"]
version = config["version"]

def ask_ai(prompt):
    data = {
        "model": model,
        "prompt": prompt,
        "stream": False
    }

    try:
        response = requests.post(url, json=data)
        result = response.json()
        return result["response"]

    except Exception:
        return (
            "\n❌ Unable to connect to Ollama.\n\n"
            "Please check:\n"
            "• Ollama is running\n"
            "• Your phone and PC are on the same Wi-Fi\n"
            "• The IP address in config.json is correct"
            )
    

