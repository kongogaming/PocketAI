import requests

from config import config


def create_embedding(text: str) -> list[float]:
    return create_embeddings([text])[0]


def create_embeddings(texts: list[str]) -> list[list[float]]:
    if not texts:
        return []

    url = config["url"].replace("/api/chat", "/api/embed")

    data = {
        "model": config["embedding_model"],
        "input": texts,
    }

    try:
        response = requests.post(
            url,
            json=data,
            timeout=60,
        )

        response.raise_for_status()

    except requests.RequestException as error:
        raise RuntimeError(
            f"Failed to create embeddings: {error}"
        ) from error

    return response.json()["embeddings"]