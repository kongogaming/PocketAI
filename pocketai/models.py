import requests
from config import config
import json
import difflib

def list_models():
    url = config["url"].replace("/api/chat", "/api/tags")

    try:
        response = requests.get(url, timeout=5)
        response.raise_for_status()

        data = response.json()

        return data.get("models", [])

    except Exception as e:
        return str(e)
    

def current_model():
    models = list_models()

    if isinstance(models, str):
        return models

    for model in models:
        if model["name"] == config["model"]:
            return model

    return None


def set_model(model_name):

    if not model_exists(model_name):
        return False

    config["model"] = model_name

    with open("config.json", "w", encoding="utf-8") as file:
        json.dump(config, file, indent=4)

    return True

def suggest_models(model_name):
    models = list_models()

    if isinstance(models, str):
        return []

    names = [model["name"] for model in models]

    return difflib.get_close_matches(
        model_name,
        names,
        n=3,
        cutoff=0.3,
    )

def model_exists(model_name):
    models = list_models()

    if isinstance(models, str):
        return False

    return any(model["name"] == model_name for model in models)