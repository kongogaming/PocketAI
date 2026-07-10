from rich.console import Console
from rich.panel import Panel
from rich.table import Table
from rich.text import Text
import random
from config import config
from theme import get_theme, get_theme_name, get_theme_icon, set_theme, list_themes, THEMES, ALIASES
console = Console()
TIPS = [
    "Use /help to view all commands.",
    "Use /theme to customize PocketAI.",
    "Enable /stats on for response benchmarks.",
    "Use /config to inspect current settings.",
    "Save conversations anytime with /save.",
    "View saved chats using /history.",
    "Reload a previous chat with /load.",
    "Rename chats using /rename.",
    "Delete unwanted chats using /delete.",
    "Everything stays local with Ollama.",
]

def get_server():
    return (
        config["url"]
        .replace("http://", "")
        .replace("https://", "")
        .replace("/api/chat", "")
    )

def show_dashboard(stats_enabled):
    
    server = get_server()

    stats = "🟢 ON" if stats_enabled else "🔴 OFF"

    table = create_info_table()

    table.add_row("🚀", "Local AI Assistant powered by Ollama")
    table.add_row("", "")
    table.add_row("🌐 Server", server)
    table.add_row("🧠 Model", config["model"])
    table.add_row("🔒 Privacy", "Local Only")
    table.add_row("📦 Version", f"v{config['version']}")
    table.add_row("📊 Statistics", stats)
    table.add_row("💬 Memory", "Conversation History")
    table.add_row("🎨 Theme", f"{get_theme_icon()} {get_theme_name()}")   
    console.print()

    show_panel(
        f"🤖 PocketAI v{config['version']}",
        table,
        "Ready • Type /help for commands",
    )
    console.print(f"[dim]💡 Tip: {random.choice(TIPS)}[/dim]")

def show_help():
    theme = get_theme()
    help_text = Text()

    def add_section(title):
        help_text.append(f"\n{title}\n", style=f"bold {theme['primary']}")
        help_text.append("═" * 70 + "\n", style=theme["border"])

    def add_cmd(icon, cmd, desc):
        help_text.append(f" {icon} ")
        help_text.append(cmd.ljust(18), style=theme["secondary"])
        help_text.append(f"{desc}\n")

    add_section("📚 GENERAL")
    add_cmd("❓", "/help", "Show this help menu")
    add_cmd("ℹ️", "/about", "About PocketAI")
    add_cmd("🏷️", "/version", "Show PocketAI version")

    add_section("💬 CONVERSATION")
    add_cmd("🧹", "/reset", "Clear conversation memory")

    add_section("💾 STORAGE")
    add_cmd("💾", "/save", "Save current conversation")
    add_cmd("📚", "/history", "View saved conversations")
    add_cmd("📂", "/load <id>", "Load a saved conversation")
    add_cmd("✏️", "/rename", "Rename a saved conversation")
    add_cmd("🗑️", "/delete", "Delete a saved conversation")

    add_section("📊 STATISTICS")
    add_cmd("📈", "/stats", "Show statistics status")
    add_cmd("🟢", "/stats on", "Enable response statistics")
    add_cmd("🔴", "/stats off", "Disable response statistics")

    add_section("🎨 APPEARANCE")
    add_cmd("🎨", "/theme", "Browse available themes")
    add_cmd("✨", "/theme <name>", "Change the current theme")

    add_section("⚙️ SYSTEM")
    add_cmd("🔧", "/config", "Display current configuration")
    add_cmd("🖥️", "/clear", "Clear the terminal")
    add_cmd("🚪", "/bye", "Exit PocketAI")

    console.print(
        Panel(
            help_text,
            title="📖 PocketAI Help",
            subtitle="🚀 Happy Coding with PocketAI!",
            border_style=theme["border"],
            padding=(1, 2),
            expand=True,
        )
    )

def show_about():
    table = create_info_table()

    table.add_row("🤖", "PocketAI")
    table.add_row("", "Lightweight Local AI Terminal Assistant")
    table.add_row("", "")

    table.add_row("📦 Version", f"v{config['version']}")
    table.add_row("👨‍💻 Author", "Somya Ranjan Pal")
    table.add_row("🐍 Language", "Python")
    table.add_row("⚡ Backend", "Ollama Chat API")
    table.add_row("🎨 UI", "Rich")
    table.add_row("🔒 Privacy", "100% Local")
    table.add_row("📄 License", "MIT")

    table.add_row("", "")
    table.add_row("✨ Features", "")
    table.add_row("", "• Local AI Chat")
    table.add_row("", "• Conversation Memory")
    table.add_row("", "• Save & Load Chats")
    table.add_row("", "• Chat History Manager")
    table.add_row("", "• Theme Support")
    table.add_row("", "• Performance Statistics")

    table.add_row("", "")
    table.add_row("❤️", "Made with Python & Rich")

    show_panel(
        "ℹ️ About PocketAI",
        table,
        "Local • Private • Fast"
    )

def show_config(stats_enabled):

    server = get_server()

    stats = "🟢 Enabled" if stats_enabled else "🔴 Disabled"

    table = create_info_table()

    table.add_row("🌐 Server", server)
    table.add_row("🧠 Model", config["model"])
    table.add_row("📦 Version", f"v{config['version']}")
    table.add_row("🎨 Theme", f"{get_theme_icon()} {get_theme_name()}")

    table.add_row("", "")

    table.add_row("📊 Statistics", stats)
    table.add_row("💬 Memory", "Conversation History")
    table.add_row("💾 Storage", "./chats/")
    table.add_row("🔒 Privacy", "100% Local")

    table.add_row("", "")

    table.add_row("⚡ Backend", "Ollama Chat API")
    table.add_row("🐍 Runtime", "Python")

    show_panel(
        "⚙️ Configuration",
        table,
        "PocketAI Settings"
    )
    
def show_stats(stats):
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

    table = create_info_table()

    table.add_row("⏱ Total Time", f"{total_time:.2f} s")
    table.add_row("⚡ Generation", f"{eval_speed:.2f} tok/s")
    table.add_row("📝 Prompt", f"{prompt_speed:.2f} tok/s")
    table.add_row("🤖 Output", f"{stats['eval_count']} tokens")
    table.add_row("📥 Prompt", f"{stats['prompt_eval_count']} tokens")

    show_panel(
        "📊 Response Statistics",
        table,
        "Ollama Performance"
    )

def show_stats_status(stats_enabled):
    status_text = "🟢 Enabled" if stats_enabled else "🔴 Disabled"

    table = create_info_table()

    table.add_row("📊 Status", status_text)
    table.add_row("", "")
    table.add_row("⚡ /stats on", "Enable response statistics")
    table.add_row("🔴 /stats off", "Disable response statistics")

    show_panel(
        "📊 Statistics",
        table,
        "Performance Monitoring"
    )

def show_reset():
    table = create_info_table()
    table.add_row("✅ Status", "Conversation history cleared")
    table.add_row("💬 Next", "Start a fresh conversation!")

    show_panel(
        "🧹 Conversation Reset",
        table,
        "Memory Cleared"
    )

def show_version():
    table = create_info_table()
    table.add_row("📦 Version", f"v{config['version']}")
    table.add_row("🧠 Model", config["model"])
    table.add_row("🐍 Python", "3.13+")
    table.add_row("💾 Storage", "Chat Manager")
    table.add_row("🎨 Themes", str(len(THEMES)))
    table.add_row("⚡ Backend", "Ollama Chat API")
    table.add_row("🎨 UI", "Rich")
    table.add_row("🔒 Privacy", "Local Only")

    show_panel(
        "📦 PocketAI Version",
        table,
        "Stable Release"
    )

def create_info_table():
    theme = get_theme()
    table = Table.grid(padding=(0,2))

    table.add_column(
        style=f"bold {theme['accent']}",
        justify="right",
        no_wrap=True,
    )
    table.add_column(style=theme["secondary"])

    return table

def show_panel(title, body, subtitle=None):
    theme = get_theme()
    console.print(
        Panel(
            body,
            title=title,
            subtitle=subtitle,
            border_style=theme["border"],
            padding=(1, 2),
            expand=True,
        )
    )

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

def show_success(message):
    show_panel("✅ Success", message, "PocketAI")

def show_warning(message):
    show_panel("⚠️ Warning", message, "PocketAI")

def show_error(message):
    show_panel("❌ Error", message, "PocketAI")

def list_themes():
    return THEMES.items()

def show_theme():
    table = create_info_table()
    current = get_theme()

    table.add_row(
        "🎨 Current",
        f"{current['icon']} {current['name']}"
    )

    table.add_row("", "")
    table.add_row("📚 Available", "")
    table.add_row("", "")
    
    for key, theme in list_themes():

        table.add_row(
            f"{theme['icon']} {theme['name']}",
            theme["description"]
        )

        aliases = [
            alias
            for alias, target in ALIASES.items()
            if target == key and alias != key
        ]

        if aliases:
            table.add_row(
                "",
                "↳ Aliases: " + ", ".join(aliases)
            )

        table.add_row("", "")

    table.add_row("💡 Usage", "/theme <name>")
    table.add_row("", "Example: /theme cyber")

    show_panel(
        "🎨 Theme Manager",
        table,
        "Customize PocketAI"
    )

def show_history(chats):
    if not chats:
        table = create_info_table()

        table.add_row("📭", "No saved conversations")
        table.add_row("", "")
        table.add_row("💾", "Use /save to save the current chat")

        show_panel(
            "📚 Chat History",
            table,
            "PocketAI Storage"
        )
        return

    table = create_info_table()

    table.add_row("📚 Saved Chats", str(len(chats)))
    table.add_row("", "")

    for i, chat in enumerate(chats, start=1):
        table.add_row(
            f"#{i}",
            f"📄 {chat['title']}"
        )

        table.add_row(
            "",
            f"📅 {chat['created']}"
        )

        table.add_row(
            "",
            f"🧠 {chat['model']}"
        )

        count = chat["messages"]
        label = "Message" if count == 1 else "Messages"

        table.add_row(
            "",
            f"💬 {count} {label}"
        )

        table.add_row(
            "",
            f"📁 {chat['filename']}"
        )

        table.add_row("", "")

    table.add_row("💡 Commands", "")
    table.add_row("", "/load <id>      Load chat")
    table.add_row("", "/rename <id>    Rename chat")
    table.add_row("", "/delete <id>    Delete chat")

    show_panel(
        "📚 Chat History",
        table,
        "PocketAI Storage"
    )

def show_usage(command, usage, example):
    table = create_info_table()

    table.add_row("⚠️ Command", command)
    table.add_row("📖 Usage", usage)
    table.add_row("💡 Example", example)

    show_panel(
        "Command Usage",
        table,
        "PocketAI Help"
    )