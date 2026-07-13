import json
import os
import sys

if getattr(sys, "frozen", False):
    BASE_DIR = os.path.dirname(sys.executable)
else:
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

CONFIG_PATH = os.path.join(BASE_DIR, "config.json")

with open(CONFIG_PATH, encoding="utf-8") as file:
    config = json.load(file)


def save_config():
    with open(CONFIG_PATH, "w", encoding="utf-8") as file:
        json.dump(config, file, indent=4)