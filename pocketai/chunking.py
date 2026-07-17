DEFAULT_CHUNK_SIZE = 500
DEFAULT_OVERLAP = 50


def chunk_text(
    text,
    chunk_size=DEFAULT_CHUNK_SIZE,
    overlap=DEFAULT_OVERLAP,
):
    words = _split_words(text)

    return _build_chunks(words, chunk_size, overlap)


def _split_words(text):
    return text.split()


def _build_chunks(words, chunk_size, overlap):
    if overlap >= chunk_size:
        raise ValueError("overlap must be smaller than chunk_size")

    chunks = []

    step = chunk_size - overlap

    for i in range(0, len(words), step):
        chunk = words[i:i + chunk_size]

        if not chunk:
            break

        chunks.append(" ".join(chunk))

    return chunks