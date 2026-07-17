from pathlib import Path

from config import load_config
from ai import ask_rag
from chunking import chunk_text
from documents import add_document
from embeddings import (
    create_embedding,
    create_embeddings,
)
from loaders import load_document
from vectors import ( add_vectors, search_vectors,)


def index_document(path: str) -> int:
    path = Path(path)

    text = load_document(path)

    chunks = chunk_text(text)

    embeddings = create_embeddings(chunks)

    success, document = add_document(path)

    if not success:
        raise RuntimeError(document)

    add_vectors(
        document_id=document["id"],
        document_name=document["name"],
        chunks=chunks,
        embeddings=embeddings,
    )

    return document["id"]


def ask_document(question: str):
    config = load_config()

    query_embedding = create_embedding(question)

    results = search_vectors(
        embedding=query_embedding,
        document_ids=config.get("active_documents"),
    )

    if (
        not results["documents"]
        or not results["documents"][0]
    ):
        return iter(
            [
                {
                    "done": True,
                    "response": (
                        "I couldn't find any relevant "
                        "information in the uploaded documents."
                    ),
                }
            ]
        ), []

    context_parts = []
    source_names = []

    for document, metadata in zip(
        results["documents"][0],
        results["metadatas"][0],
    ):
        context_parts.append(
            (
                f"Source: {metadata['document_name']}\n\n"
                f"{document}"
            )
        )

        name = metadata["document_name"]
        if name not in source_names:
            source_names.append(name)

    context = "\n\n------------------------\n\n".join(
        context_parts
    )

    return ask_rag(question, context), source_names