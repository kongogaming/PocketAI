import json
import os
import sys
from pathlib import Path

if getattr(sys, "frozen", False):
    BASE_DIR = os.path.dirname(sys.executable)
else:
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

CONFIG_PATH = os.path.join(BASE_DIR, "config.json")

config = {}


def load_config():
    with open(CONFIG_PATH, encoding="utf-8") as file:
        data = json.load(file)

    config.clear()
    config.update(data)

    return config


def save_config():
    with open(CONFIG_PATH, "w", encoding="utf-8") as file:
        json.dump(config, file, indent=4)