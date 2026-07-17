import chromadb
from config import save_config, load_config
from pathlib import Path

VECTOR_DB = Path("vectors")

client = None
collection = None


def initialize() -> None:
    global client, collection

    client = chromadb.PersistentClient(
        path=str(VECTOR_DB)
    )

    collection = client.get_or_create_collection(
        name="documents"
    )


def add_vectors(
    document_id: int,
    document_name: str,
    chunks: list[str],
    embeddings: list[list[float]],
) -> None:
    if collection is None:
        raise RuntimeError(
            "Vector database has not been initialized."
        )

    if len(chunks) != len(embeddings):
        raise ValueError(
            "Number of chunks and embeddings must match."
        )

    ids = []
    metadatas = []

    for index in range(len(chunks)):
        ids.append(f"{document_id}_{index}")

        metadatas.append(
            {
                "document_id": document_id,
                "document_name": document_name,
                "chunk_index": index,
            }
        )

    collection.add(
        ids=ids,
        documents=chunks,
        embeddings=embeddings,
        metadatas=metadatas,
    )


def search_vectors(
    embedding: list[float],
    limit: int = 5,
    document_ids: list[int] | None = None,
) -> dict:
    if collection is None:
        raise RuntimeError(
            "Vector database has not been initialized."
        )

    query: dict = {
        "query_embeddings": [embedding],
        "n_results": limit,
    }

    if document_ids is not None:
        query["where"] = {
            "document_id": {
                "$in": document_ids,
            }
        }

    return collection.query(**query)


def delete_document(document_id: int) -> None:
    if collection is None:
        raise RuntimeError(
            "Vector database has not been initialized."
        )

    collection.delete(
        where={
            "document_id": document_id,
        }
    )


def get_chunk_count(document_id: int) -> int:
    if collection is None:
        return 0

    results = collection.get(
        where={"document_id": document_id}
    )

    return len(results["ids"])


def clear_database() -> None:
    global collection

    if client is None:
        raise RuntimeError(
            "Vector database has not been initialized."
        )

    client.delete_collection("documents")

    collection = client.get_or_create_collection(
        name="documents"
    )

