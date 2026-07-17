from pathlib import Path
import json
import shutil
from datetime import datetime

DOCUMENTS_DIR = Path("documents")
DATA_DIR = Path("data")
DOCUMENTS_DB = DATA_DIR / "documents.json"


def initialize():
    DOCUMENTS_DIR.mkdir(exist_ok=True)

    DATA_DIR.mkdir(exist_ok=True)

    if not DOCUMENTS_DB.exists():
        with open(DOCUMENTS_DB, "w", encoding="utf-8") as file:
            json.dump([], file, indent=4)

def load_documents():
    initialize()

    with open(DOCUMENTS_DB, "r", encoding="utf-8") as file:
        return json.load(file)
    
def save_documents(documents):
    initialize()

    with open(DOCUMENTS_DB, "w", encoding="utf-8") as file:
        json.dump(documents, file, indent=4)
        
def document_exists(filename):
    documents = load_documents()

    for document in documents:
        if document["name"] == filename:
            return True

    return False

def add_document(path):
    initialize()

    path = Path(path)

    if not path.exists():
        return False, "File not found."

    if document_exists(path.name):
        return False, "Document already exists."

    destination = DOCUMENTS_DIR / path.name

    shutil.copy2(path, destination)

    documents = load_documents()

    document = {
        "id": len(documents) + 1,
        "name": path.name,
        "type": path.suffix.lower().replace(".", ""),
        "size": path.stat().st_size,
        "added": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
    }

    documents.append(document)

    save_documents(documents)

    return True, document

def remove_document(document_id: int) -> tuple[bool, dict | str]:
    documents = load_documents()

    for document in documents:
        if document["id"] == document_id:

            file_path = DOCUMENTS_DIR / document["name"]

            if file_path.exists():
                file_path.unlink()

            documents.remove(document)

            save_documents(documents)

            return True, document

    return False, "Document not found."

def clear_documents() -> None:
    documents = load_documents()

    for document in documents:
        file_path = DOCUMENTS_DIR / document["name"]

        if file_path.exists():
            file_path.unlink()

    save_documents([])


def get_document(document_id: int):
    documents = load_documents()

    for document in documents:
        if document["id"] == document_id:
            return document

    return None
