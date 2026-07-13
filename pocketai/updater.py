from config import config


def get_current_version():
    return config["version"]


def get_latest_version():
    return config["version"]


def is_update_available():
    current = get_current_version()
    latest = get_latest_version()

    return current != latest, current, latest