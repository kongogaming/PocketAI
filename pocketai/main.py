from config import config
from ai import ask_ai
import os
def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")
def show_banner():
    server = (
        config["url"]
        .replace("http://", "")
        .replace("https://", "")
        .replace("/api/generate", "")
    )
    WIDTH = 74  
    print()
    print("┌" + "─" * WIDTH + "┐")
    print(f"│{'🤖 PocketAI':^{WIDTH}}│")
    print(f"│{'v' + config['version'] :^{WIDTH}}│")
    print("├" + "─" * WIDTH + "┤")
    print(f"│{'🚀 Local AI Assistant powered by Ollama':^{WIDTH}}│")
    print(f"│{'':<{WIDTH}}│")
    print(f"│ {'🌐 Server':<10}: {server:<58}  │")
    print(f"│ {'🧠 Model':<10}: {config['model']:<58}  │")
    print(f"│ {'🔒 Mode':<10}: {'Local Only':<58}  │")
    print("├" + "─" * WIDTH + "┤")
    print(f"│ {'Type /help to view available commands.':<{WIDTH-1}}│")
    print("└" + "─" * WIDTH + "┘")
    print()
def show_help():
    WIDTH = 74
    print()
    print("┌" + "─" * WIDTH + "┐")
    print(f"│{'📖 PocketAI Help':^{WIDTH}}│")
    print("├" + "─" * WIDTH + "┤")
    print(f"│{'':<{WIDTH}}│")
    print(f"│{'💬 Available Commands':^{WIDTH}}│")
    print(f"│{'':<{WIDTH}}│")
    print(f"│  {'/help':<10}  Show this help menu{'':<{WIDTH-34}}│")
    print(f"│  {'/config':<10}  Display current configuration{'':<{WIDTH-44}}│")
    print(f"│  {'/clear':<10}  Clear the screen{'':<{WIDTH-33}}│")
    print(f"│  {'/bye':<10}  Exit PocketAI{'':<{WIDTH-30}}│")
    print(f"│{'':<{WIDTH}}│")
    print("├" + "─" * WIDTH + "┤")
    print(f"│{'🚀 Happy Coding with PocketAI!':^{WIDTH}}│")
    print("└" + "─" * WIDTH + "┘")
    print()
def show_config():
    server = (
        config["url"]
        .replace("http://", "")
        .replace("https://", "")
        .replace("/api/generate", "")
    )
    WIDTH = 74
    print()
    print("┌" + "─" * WIDTH + "┐")
    print(f"│{'⚙️ PocketAI Config':^{WIDTH}} │")
    print("├" + "─" * WIDTH + "┤")
    print(f"│{'':<{WIDTH}}│")
    print(f"│  {'🌐 Connected Server':<20}: {server:<46}   │")
    print(f"│  {'🧠 Active Model':<20}: {config['model']:<46}   │")
    print(f"│  {'📦 Version':<20}: v{config['version']:<45}   │")
    print(f"│  {'🔒 Privacy':<20}: {'Local Only':<46}   │")
    print(f"│{'':<{WIDTH}}│")
    print("├" + "─" * WIDTH + "┤")
    print(f"│{'Configuration loaded successfully.':^{WIDTH}}│")
    print("└" + "─" * WIDTH + "┘")
    print()
def main():
    clear_screen()
    show_banner()

    while True:
        prompt = input("You > ")

        if not prompt.strip():
            continue

        if prompt.lower() == "/bye":
            print("🤖 PocketAI > Goodbye! 👋")
            break

        if prompt.lower() == "/help":
            show_help()
            continue

        if prompt.lower() == "/clear":
            clear_screen()
            show_banner()
            continue

        if prompt.lower() == "/config":
            show_config()
            continue

        print()
        print("🧠 PocketAI is thinking...", end="", flush=True)

        result = ask_ai(prompt)

        print("\r" + " " * 80, end="\r")
        print("🤖 PocketAI >", result)
        print()

if __name__ == "__main__":
    main()