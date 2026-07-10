import json
from config import config
import requests 

url = config["url"]
model = config["model"]
version = config["version"]

def ask_ai(history):
    data = {
        "model": model,
        "messages": history,
        "stream": True
    }

    try:
        response = requests.post(url, json=data, stream=True)
        response.raise_for_status()
        full_response = ""
        first_chunk = True
        for line in response.iter_lines():
            if not line:
                continue
            
            result= json.loads(line)
            chunk = result.get("message", {}).get("content", "")
            
            if first_chunk:
                print("\r" + " " * 100, end="\r")
                print("🤖 PocketAI >", end=" ", flush=True)
                first_chunk = False

            if chunk:
                print(chunk, end="", flush=True)
                full_response += chunk
            
            if result["done"]:
                stats = {
                    "total_duration": result.get("total_duration"),
                    "eval_count": result.get("eval_count"),
                    "eval_duration": result.get("eval_duration"),
                    "prompt_eval_count": result.get("prompt_eval_count"),
                    "prompt_eval_duration": result.get("prompt_eval_duration"),
                }
                break
        return{
            "response": full_response,
            "stats": stats
        }

    except Exception:
        return (
            "\n❌ Unable to connect to Ollama.\n\n"
            "Please check:\n"
            "• Ollama is running\n"
            "• Please check:"
            "• Ollama is running\n"
            "• The server address is correct\n"
            "• Ollama is accessiblei\n"
            "• The IP address in config.json is correct"
            )
    

