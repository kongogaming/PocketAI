

from config import config
from ai import ask_ai
import os
import random

def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")

def show_banner():
    server = (
        config["url"]
        .replace("http://", "")
        .replace("https://", "")
        .replace("/api/chat", "")
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

    print(f"│  {'/help':<12} Show this help menu{'':<{WIDTH-35}}│")
    print(f"│  {'/about':<12} About PocketAI{'':<{WIDTH-31}}│")
    print(f"│  {'/config':<12} Display current configuration{'':<{WIDTH-44}}│")
    print(f"│  {'/stats':<12} Show statistics settings{'':<{WIDTH-39}}│")
    print(f"│  {'/stats on':<12} Enable response statistics{'':<{WIDTH-42}}│")
    print(f"│  {'/stats off':<12} Disable response statistics{'':<{WIDTH-43}}│")
    print(f"│  {'/version':<12} Show PocketAI version{'':<{WIDTH-38}}│")
    print(f"│  {'/reset':<12} Reset conversation memory{'':<{WIDTH-40}}│")
    print(f"│  {'/clear':<12} Clear the console screen{'':<{WIDTH-39}}│")
    print(f"│  {'/bye':<12} Exit PocketAI{'':<{WIDTH-31}}│")

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
        .replace("/api/chat", "")
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

STATUS_MESSAGES = {
    "thinking": [
        "🧠 PocketAI is thinking...",
        "💭 PocketAI is processing your request..."
    ],
    "searching": [
        "🔍 PocketAI is searching for the best response...",
        "📚 PocketAI is gathering information..."
    ],
    "writing": [
        "✨ PocketAI is crafting a response...",
        "📝 PocketAI is writing your answer..."
    ]
}
def status():
    category = random.choice(list(STATUS_MESSAGES.keys()))
    return random.choice(STATUS_MESSAGES[category])

def show_stats(stats):
    WIDTH = 50

    total_time = stats["total_duration"] / 1_000_000_000

    eval_speed = (
        stats["eval_count"] /
        (stats["eval_duration"] / 1_000_000_000)
        if stats["eval_duration"] else 0
    )

    prompt_speed = (
        stats["prompt_eval_count"] /
        (stats["prompt_eval_duration"] / 1_000_000_000)
        if stats["prompt_eval_duration"] else 0
    )

    print()
    print("┌" + "─" * WIDTH + "┐")
    print(f"│{'📊 Response Statistics':^{WIDTH}}│")
    print("├" + "─" * WIDTH + "┤")
    print(f"│ ⏱ Total Time   : {total_time:>8.2f} s{'':<{WIDTH-29}}│")
    print(f"│ ⚡ Eval Speed   : {eval_speed:>8.2f} tok/s{'':<{WIDTH-33}}│")
    print(f"│ 📝 Prompt Speed : {prompt_speed:>8.2f} tok/s{'':<{WIDTH-35}}│")
    print("└" + "─" * WIDTH + "┘")

def show_stats_status():
    WIDTH = 50

    status = "🟢 ON" if stats_enabled else "🔴 OFF"

    print()
    print("┌" + "─" * WIDTH + "┐")
    print(f"│{'📊 Statistics':^{WIDTH}}│")
    print("├" + "─" * WIDTH + "┤")
    print(f"│ {'Status':<12}: {status:<34}│")
    print("├" + "─" * WIDTH + "┤")
    print(f"│ {'/stats on':<12} Enable response statistics{'':<{WIDTH-39}}│")
    print(f"│ {'/stats off':<12} Disable response statistics{'':<{WIDTH-40}}│")
    print("└" + "─" * WIDTH + "┘")
    print()

def show_reset():
    WIDTH = 50

    print()
    print("┌" + "─" * WIDTH + "┐")
    print(f"│{'🧹 Conversation Reset':^{WIDTH}}│")
    print("├" + "─" * WIDTH + "┤")
    print(f"│{'Conversation history has been cleared.':^{WIDTH}}│")
    print(f"│{'Start a fresh conversation!':^{WIDTH}}│")
    print("└" + "─" * WIDTH + "┘")
    print()

def show_version():
    WIDTH = 50

    print()
    print("┌" + "─" * WIDTH + "┐")
    print(f"│{'ℹ️ PocketAI Version':^{WIDTH}}│")
    print("├" + "─" * WIDTH + "┤")
    print(f"│ {'Version':<12}: v{config['version']:<31}│")
    print(f"│ {'Model':<12}: {config['model']:<32}│")
    print(f"│ {'Mode':<12}: {'Local Only':<32}│")
    print(f"│ {'Author':<12}: {'Somya Ranjan Pal':<32}│")
    print("└" + "─" * WIDTH + "┘")
    print()

def show_about():
    WIDTH = 74

    print()
    print("┌" + "─" * WIDTH + "┐")
    print(f"│{'ℹ️ About PocketAI':^{WIDTH}}│")
    print("├" + "─" * WIDTH + "┤")
    print(f"│{'':<{WIDTH}}│")
    print(f"│{'PocketAI is a lightweight local AI assistant':^{WIDTH}}│")
    print(f"│{'built on top of Ollama for fast offline chats.':^{WIDTH}}│")
    print(f"│{'':<{WIDTH}}│")
    print(f"│ {'Version':<12}: v{config['version']:<52}│")
    print(f"│ {'Author':<12}: Somya Ranjan Pal{'':<45}│")
    print(f"│ {'Backend':<12}: Ollama Chat API{'':<43}│")
    print(f"│ {'Mode':<12}: Local Only{'':<48}│")
    print(f"│{'':<{WIDTH}}│")
    print("├" + "─" * WIDTH + "┤")
    print(f"│{'Made with ❤️  and Python':^{WIDTH}}│")
    print("└" + "─" * WIDTH + "┘")
    print()

stats_enabled = False
def main():
    global stats_enabled
    
    clear_screen()
    show_banner()
    history = []
    while True:
        print()
        prompt = input("You > ")

        if not prompt.strip():
            continue

        if prompt.lower() == "/bye":
            print("🤖 PocketAI > Goodbye! 👋")
            break

        if prompt.lower() == "/stats":
            show_stats_status()
            continue
                
        if prompt.lower() == "/help":
            show_help()
            continue
        
        if prompt.lower() == "/about":
            show_about()
            continue
        
        if prompt.lower() == "/reset":
            history.clear()
            show_reset()
            continue
        
        if prompt.lower() == "/version":
            show_version()
            continue

        if prompt.lower() == "/clear":
            clear_screen()
            show_banner()
            continue

        if prompt.lower() == "/stats on":
            stats_enabled = True
            show_stats_status()
            continue

        if prompt.lower() == "/stats off":
            stats_enabled = False
            show_stats_status()
            continue
        
        if prompt.lower() == "/config":
            show_config()
            continue
        history.append({
            "role": "user",
            "content": prompt
        })
        print()
        print(status(), end="", flush=True)
        
        result = ask_ai(history)
        if isinstance(result, str):
            print(result)
            continue
        response = result["response"]
        stats = result["stats"]
        
        print()
        
        history.append({
            "role": "assistant",
            "content": response
        })
        
        if stats_enabled:
            show_stats(stats)

if __name__ == "__main__":
    main()