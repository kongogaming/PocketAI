# theme.py

THEMES = {
    "default": {
        "icon": "🎨",
        "name": "Default",
        "description": "Classic PocketAI",
        "primary": "cyan",
        "secondary": "green",
        "accent": "yellow",
        "border": "cyan",
        "dim": "dim",
    },

    "ocean": {
        "icon": "🌊",
        "name": "Ocean",
        "description": "Blue Ocean",

        "primary": "bright_cyan",
        "secondary": "bright_blue",
        "accent": "white",
        "border": "bright_cyan",
        "dim": "dim",
    },
    
    "matrix": {
        "icon": "💚",
        "name": "Matrix",
        "description": "Hacker Green",

        "primary": "green",
        "secondary": "bright_green",
        "accent": "white",
        "border": "green",
        "dim": "dim",
    },
    "cyber": {
        "icon": "⚡",
        "name": "Cyber",
        "description": "Neon Cyberpunk",

        "primary": "bright_magenta",
        "secondary": "bright_cyan",
        "accent": "bright_yellow",
        "border": "bright_magenta",
        "dim": "dim",
    },
    "nord": {
        "icon": "❄️",
        "name": "Nord",
        "description": "Arctic Blue",

        "primary": "bright_blue",
        "secondary": "cyan",
        "accent": "white",
        "border": "bright_blue",
        "dim": "dim",
    },
    "dracula": {
        "icon": "🧛",
        "name": "Dracula",
        "description": "Purple Night",

        "primary": "magenta",
        "secondary": "bright_magenta",
        "accent": "bright_white",
        "border": "magenta",
        "dim": "dim",
    },
    }

    

ALIASES = {
   
    "default": "default",
    "classic": "default",

    "ocean": "ocean",
    "blue": "ocean",
    "blue ocean": "ocean",
  
    "matrix": "matrix",
    "green": "matrix",
    "hacker": "matrix",

    "cyber": "cyber",
    "cyberpunk": "cyber",
    "neon": "cyber",

    "dracula": "dracula",
    "purple": "dracula",
    "vampire": "dracula",
    
    "nord": "nord",
    "nord blue": "nord",
    "ice": "nord",
}

current_theme = "default"


def get_theme():
    return THEMES[current_theme]


def get_theme_name():
    return THEMES[current_theme]["name"]


def get_theme_icon():
    return THEMES[current_theme]["icon"]

def set_theme(name):
    global current_theme

    name = name.strip().lower()

    if name in ALIASES:
        current_theme = ALIASES[name]
        return True

    return False
def list_themes():
    return THEMES.items()