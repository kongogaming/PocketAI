import json
from config import config
import requests 

def ask_ai_stream(history):
    url = config["url"]
    model = config["model"]
    version = config["version"]
    data = {
        "model": model,
        "messages": history,
        "stream": True,
    }

    try:
        response = requests.post(url, json=data, stream=True, timeout=(10, 300))
        response.encoding = "utf-8"
        response.raise_for_status()

        full_response = ""

        for line in response.iter_lines():
            if not line:
                continue

            result = json.loads(line)

            chunk = result.get("message", {}).get("content", "")

            if chunk:
                full_response += chunk

                yield {
                    "done": False,
                    "chunk": chunk,
                }

            if result.get("done", False):

                stats = {
                    "total_duration": result.get("total_duration"),
                    "eval_count": result.get("eval_count"),
                    "eval_duration": result.get("eval_duration"),
                    "prompt_eval_count": result.get("prompt_eval_count"),
                    "prompt_eval_duration": result.get("prompt_eval_duration"),
                }

                yield {
                    "done": True,
                    "response": full_response,
                    "stats": stats,
                }

                return

    except Exception:
        yield {
            "done": True,
            "error": (
                "\n❌ Unable to connect to Ollama.\n\n"
                "Please check:\n"
                "• Ollama is running\n"
                "• The server address is correct\n"
                "• Ollama is accessible\n"
                "• The IP address in config.json is correct"
            ),
        }

def ask_rag(question: str, context: str):
    system_prompt = f"""
You are PocketAI.

Answer the user's question using ONLY the provided context.

If the answer cannot be found in the context, say:

"I couldn't find that information in the uploaded documents."

Context:

{context}
"""

    messages = [
        {
            "role": "system",
            "content": system_prompt,
        },
        {
            "role": "user",
            "content": question,
        },
    ]

    return ask_ai_stream(messages)