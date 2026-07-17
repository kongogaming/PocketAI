from pathlib import Path
from pypdf import PdfReader
from docx import Document
SUPPORTED_EXTENSIONS = {
    ".txt",
    ".md",
    ".pdf",
    ".docx",
}


def load_document(path):
    path = Path(path)

    extension = path.suffix.lower()

    if extension == ".txt":
        return _load_txt(path)

    elif extension == ".md":
        return _load_md(path)

    elif extension == ".pdf":
        return _load_pdf(path)

    elif extension == ".docx":
        return _load_docx(path)

    raise ValueError(f"Unsupported file type: {extension}")

def _load_txt(path):
    with open(path, "r", encoding="utf-8") as file:
        return file.read()
    
def _load_md(path):
    with open(path, "r", encoding="utf-8") as file:
        return file.read()
    
def _load_pdf(path):
    reader = PdfReader(path)

    text = []

    for page in reader.pages:
        page_text = page.extract_text()

        if page_text:
            text.append(page_text)

    return "\n\n".join(text)

def _load_docx(path):
    document = Document(path)

    text = []

    for paragraph in document.paragraphs:
        if paragraph.text.strip():
            text.append(paragraph.text)

    return "\n".join(text)

