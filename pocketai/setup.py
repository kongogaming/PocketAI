import json
import requests
from rich.prompt import Confirm, Prompt 
from pathlib import Path
from setup_ui import (
    show_welcome,
    show_server_help,
    show_connection_check,
    show_connection_success,
    show_connection_error,
    show_no_models,
    show_models,
    show_setup_complete,
    show_creating_config,
)
import os
import time
from rich.console import Console
console = Console()

CONFIG_FILE = Path("config.json")
def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")

def is_first_run():
    return not CONFIG_FILE.exists()

def ask_server():
    
    server = Prompt.ask(
            "[bold]Server[/]",
            default="localhost"
        ).strip() 

    if not server:
        return "http://localhost:11434"

    if not server.startswith(("http://", "https://")):
        server = "http://" + server

    host = server.split("://", 1)[1]

    if ":" not in host:
        server += ":11434"

    return server

def check_connection(server):
    try:
        response = requests.get(
            f"{server}/api/tags",
            timeout=5
        )

        response.raise_for_status()

        return response.json()

    except requests.exceptions.RequestException:
        return None
    
def detect_models(data):
    models = data.get("models", [])

    if not models:
        return []

    installed = []

    for model in models:
        installed.append(model["name"])

    return installed

def recommend_model(models):
    preferred = [
        "qwen2.5:3b",
        "qwen2.5:1.5b",
        "qwen3:4b",
        "gemma3:1b",
        "phi4-mini",
        "deepseek-r1",
        "llama3.2",
        "mistral",
        "tinyllama",
    ]

    for model in preferred:
        if model in models:
            return model

    return models[0] if models else None

def choose_model(models, recommended):
    if Confirm.ask(
        f"Use the recommended model ([bold]{recommended}[/])?",
        default=True,
    ):
        return recommended
    
    selection = Prompt.ask(
        "Choose model number",
        choices=[str(i) for i in range(1, len(models) + 1)],
    )
    console.print(f"[green]✓ Selected:[/] {models[int(selection)-1]}")
    return models[int(selection) - 1]
        
def create_config(server, model):
    config = {
        "url": f"{server}/api/chat",
        "model": model,
        "theme": "Nord",
        "stats": False,
        "version": "0.5.2"
    }
    with open(CONFIG_FILE, "w", encoding="utf-8") as file:
        json.dump(config, file, indent=4)
    return config

def run_setup():
    clear_screen()
    show_welcome()

    while True:
        clear_screen()
        show_server_help()

        server = ask_server()

        show_connection_check()

        data = check_connection(server)

        if data is None:
            show_connection_error(server)

            action = connection_menu()

            if action == "retry":
                continue

            if action == "change":
                continue

            if action == "quit":
                return None
        clear_screen()
        show_connection_success(server)

        time.sleep(0.5)

        models = detect_models(data)

        if not models:
            clear_screen()
            show_no_models()
            continue

        recommended = recommend_model(models)

        show_models(models, recommended)

        model = choose_model(models, recommended)

        show_creating_config()

        config = create_config(server, model)

        time.sleep(0.5)

        clear_screen()
        show_setup_complete()

        time.sleep(2)

        return config

def connection_menu():
    while True:
        choice = Prompt.ask(
            "Choose",
            choices=["R", "C", "Q"],
            default="R"
        ).lower()

        if choice in ("r", "retry"):
            return "retry"

        if choice in ("c", "change"):
            return "change"

        if choice in ("q", "quit"):
            return "quit"

        print("❌ Please enter R, C or Q.")

