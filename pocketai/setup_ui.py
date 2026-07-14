from rich.console import Console
from rich.panel import Panel
from rich.table import Table
from rich.text import Text
from rich.prompt import Prompt
from rich.status import Status
import time
from theme import get_theme

console = Console()


def show_welcome():
    theme = get_theme()

    text = Text(justify="center")

    text.append("👋 First-Time Setup\n\n", style=f"bold {theme['primary']}")

    text.append(
        "PocketAI couldn't find a configuration file.\n\n"
    )

    text.append(
        "We'll configure everything in less than a minute.\n\n"
    )

    text.append("✓ Detect your Ollama server\n")
    text.append("✓ Detect installed AI models\n")
    text.append("✓ Create your configuration\n")
    text.append("✓ Launch PocketAI\n\n")

    text.append(
        "Press Enter to begin...",
        style=f"bold {theme['secondary']}"
    )

    console.print(
        Panel(
            text,
            title="🚀 Welcome to PocketAI",
            border_style=theme["border"],
            padding=(1, 2),
            expand=True,
        )
    )

    input()

def show_server_help():
    theme = get_theme()

    text = Text(justify="left")

    text.append(
        "Where is Ollama running?\n\n",
        style=f"bold {theme['primary']}"
    )

    text.append(
        "PocketAI needs the address of your Ollama server.\n\n"
    )

    text.append(
        "Leave blank to use localhost.\n\n"
    )

    text.append(
        "Examples\n\n",
        style=f"bold {theme['secondary']}"
    )

    text.append("  • localhost\n")
    text.append("  • 192.168.29.142\n")
    text.append("  • 192.168.29.142:11434")

    console.print(
        Panel(
            text,
            title="🌐 Ollama Server",
            border_style=theme["border"],
            padding=(1,2),
            expand=True,
        )
    )

def show_connection_check():
    theme = get_theme()
    console.print()
    with console.status(
    "Connecting to Ollama...",
    spinner="dots"
    ):
        time.sleep(0.4)
    
def show_connection_success(server):
    theme = get_theme()
    console.print()

    console.print(
        Panel(
            f"[green]✅ Successfully connected![/]\n\n"
            f"[bold]Server:[/]\n{server}",
            title="✅ Connected",
            border_style=theme["border"],
            padding=(1, 2),
            expand=True,
        )
    )
    
def show_connection_error(server):
    theme = get_theme()
    text = Text()

    text.append("❌ Unable to connect to Ollama.\n\n", style="bold red")

    text.append("Server:\n", style="bold")
    text.append(f"{server}\n\n")

    text.append("Possible reasons:\n", style="bold")

    text.append("• Ollama isn't running.\n")
    text.append("• The server address is incorrect.\n")
    text.append("• Your firewall is blocking the connection.\n")
    text.append("• Your PC and server are not on the same network.\n\n")

    text.append("[R] Retry connection\n")
    text.append("[C] Change server\n")
    text.append("[Q] Quit PocketAI")

    console.print(
        Panel(
            text,
            title="❌ Connection Failed",
            border_style=theme["border"],
            padding=(1, 2),
            expand=True,
        )
    )

def show_models(models, recommended):
    
    theme = get_theme()
    table = Table(
        title="📦 Installed Models",
        border_style=theme["border"],
    )

    table.add_column("#", style=theme["primary"], justify="center")
    table.add_column("Model", style=theme["secondary"])
    table.add_column("Status", justify="center")

    for i, model in enumerate(models, start=1):
        status = "⭐ Recommended" if model == recommended else ""
        table.add_row(str(i), model, status)

    console.print(table)

def show_no_models():
    theme = get_theme()
    console.print(
        Panel(
            f"[bold red]No Ollama models were found.[/]\n\n"
            f"Install one using:\n\n"
            f"[bold {theme['primary']}]ollama pull qwen2.5:1.5b[/]",
            title="📦 No Models Found",
            border_style=theme["border"],
            padding=(1, 2),
            expand=True,
        )
    )

def show_setup_complete():
    theme = get_theme()

    text = Text(justify="center")

    text.append(
        "Everything is configured! 🎉\n\n",
        style=f"bold {theme['primary']}"
    )

    text.append("✓ Connected to Ollama\n")
    text.append("✓ AI model selected\n")
    text.append("✓ Configuration saved\n\n")

    text.append(
        "Welcome to PocketAI! 🚀\n\n",
        style=f"bold {theme['secondary']}"
    )

    with console.status(
        "Launching PocketAI...",
        spinner="dots"
    ):
        time.sleep(1)

    console.print(
        Panel(
            text,
            title="✅ Setup Complete",
            border_style=theme["border"],
            padding=(1, 2),
            expand=True,
        )
    )

def show_creating_config():
    theme = get_theme()

    with console.status(
        f"[bold {theme['primary']}]Creating configuration...[/]",
        spinner="dots"
    ):
        time.sleep(0.7)
