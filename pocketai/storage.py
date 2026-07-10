import os
import json
from datetime import datetime
from config import config

CHAT_FOLDER = "chats"

def ensure_chat_folder():
    os.makedirs(CHAT_FOLDER, exist_ok=True)

def save_chat(history):
    ensure_chat_folder()

    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    filename = f"{timestamp}.json"

    filepath = os.path.join(CHAT_FOLDER, filename)

    title = "New Chat"

    for msg in history:
        if msg["role"] == "user":
            title = msg["content"].replace("\n", " ").strip()[:40]
            break

    data = {
        "title": title,
        "created": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "model": config["model"],
        "messages": history,
    }

    with open(filepath, "w", encoding="utf-8") as file:
        json.dump(data, file, indent=4, ensure_ascii=False)

    return filename

def list_chats():
    ensure_chat_folder()

    chats = []

    files = [
        file
        for file in os.listdir(CHAT_FOLDER)
        if file.endswith(".json")
    ]

    files.sort(reverse=True)

    for file in files:
        filepath = os.path.join(CHAT_FOLDER, file)

        with open(filepath, "r", encoding="utf-8") as f:
            data = json.load(f)
        
        chats.append({
            "title": data.get("title", "Untitled"),
            "filename": file,
            "created": data.get("created", "Unknown"),
            "model": data.get("model", "Unknown"),
            "messages": len(data.get("messages", [])),
        })
    return chats

def load_chat(index):
    chats = list_chats()

    if index < 1 or index > len(chats):
        return None

    chat = chats[index - 1]

    filepath = os.path.join(CHAT_FOLDER, chat["filename"])

    with open(filepath, "r", encoding="utf-8") as file:
        return json.load(file)
    
def delete_chat(index):
    chats = list_chats()

    if index < 1 or index > len(chats):
        return None

    chat = chats[index - 1]

    filepath = os.path.join(CHAT_FOLDER, chat["filename"])

    os.remove(filepath)

    return chat

def rename_chat(index, new_title):
    chats = list_chats()

    if index < 1 or index > len(chats):
        return None

    chat = chats[index - 1]

    filepath = os.path.join(CHAT_FOLDER, chat["filename"])

    with open(filepath, "r", encoding="utf-8") as file:
        data = json.load(file)

    data["title"] = new_title

    with open(filepath, "w", encoding="utf-8") as file:
        json.dump(data, file, indent=4, ensure_ascii=False)

    return data