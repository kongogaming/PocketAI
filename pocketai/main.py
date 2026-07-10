
from config import config
from ai import ask_ai
import os
import random
from ui import (
    show_dashboard,
    show_help,
    show_about,
    show_config,
    show_stats,
    show_stats_status,
    show_reset,
    show_version,
    status,
    show_success,
    show_warning,
    show_error,
    show_theme,
    show_history,
    show_usage,
)
from theme import get_theme, get_theme_icon, get_theme_name, set_theme, list_themes
from storage import save_chat
from storage import list_chats, load_chat, list_chats, delete_chat, rename_chat

def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")

stats_enabled = False

def main():
    global stats_enabled
    
    clear_screen()
    show_dashboard(stats_enabled)
    history = []
    try:
        while True:
            print()
            prompt = input("You > ")

            if not prompt.strip():
                continue

            if prompt.lower() == "/bye":
                show_success("Goodbye! 👋")
                break

            if prompt.lower() == "/stats":
                show_stats_status(stats_enabled)
                continue
            
            if prompt.lower() == "/history":
                files = list_chats()
                show_history(files)
                continue
            
            if prompt.lower().startswith("/delete "):
                try:
                    index = int(prompt.split()[1])
                except:
                    show_warning("Usage: /delete <number>")
                    continue
                chat = delete_chat(index)
                if chat is None:
                    show_warning("Chat not found.")
                else:
                    show_success(
                        f"Deleted '{chat['title']}'"
                    )
                continue
            
            if prompt.lower().startswith("/rename "):
                parts = prompt.split(maxsplit=2)
                if len(parts) < 3:
                    show_warning("Usage: /rename <number> <title>")
                    continue
                try:
                    index = int(parts[1])
                except ValueError:
                    show_warning("Usage: /rename <number> <title>")
                    continue

                new_title = parts[2]
                chat = rename_chat(index, new_title)
                if chat is None:
                    show_warning("Chat not found.")
                else:
                    show_success(
                        f"Renamed to '{new_title}'"
                    )
                continue
                
            if prompt.lower() == "/delete":
                show_usage(
                    "/delete",
                    "/delete <number>",
                    "/delete 1"
                )
                continue
            
            if prompt.lower() == "/load":
                show_usage(
                    "/load",
                    "/load <number>",
                    "/load 2"
                )
                continue
            
            if prompt.lower() == "/rename":
                show_usage(
                    "/rename",
                    "/rename <number> <new title>",
                    "/rename 1 Python Notes"
                )
                continue
            
            
                
            if prompt.lower().startswith("/load "):
                try:
                    index = int(prompt.split()[1])
                except:
                    show_warning("Usage: /load <number>")
                    continue
                
                chat = load_chat(index)
                if chat is None:
                    show_warning("Chat not found.")
                    continue
                history = chat["messages"]
                show_success(f"Loaded '{chat['title']}'")                   
                continue
                
            if prompt.lower() == "/save":

                if not history:
                    show_warning("Nothing to save yet.")
                    continue

                filename = save_chat(history)
                show_success(
                    f"Conversation saved.\n\n"
                    f"📁 chats/\n"
                    f"📄 {filename}"
                )
                continue
            
            if prompt.lower() == "/help":
                show_help()
                continue
            
            if prompt.lower() == "/about":
                show_about()
                continue
            
            if prompt.lower() == "/theme":
                show_theme()
                continue
            
            if prompt.lower().startswith("/theme "):
                theme_name = prompt.split(maxsplit=1)[1].lower()

                if set_theme(theme_name):
                    show_success(
                        f"Theme changed to {get_theme_icon()} {get_theme_name()}."
                    )
                else:
                    show_warning(
                        f"Unknown theme '{theme_name}'. Use /theme to see available themes."
                    )

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
                show_dashboard(stats_enabled)
                continue

            if prompt.lower() == "/stats on":
                stats_enabled = True
                show_stats_status(stats_enabled)
                continue

            if prompt.lower() == "/stats off":
                stats_enabled = False
                show_stats_status(stats_enabled)
                continue
            
            if prompt.lower() == "/config":
                show_config(stats_enabled)
                continue
            history.append({
                "role": "user",
                "content": prompt
            })
            print()
            print(status(), end="", flush=True)
            
            result = ask_ai(history)
            if isinstance(result, str):
                show_error(result)
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
                
    except KeyboardInterrupt:
        print()
        show_success("Goodbye! 👋")

if __name__ == "__main__":
    main()