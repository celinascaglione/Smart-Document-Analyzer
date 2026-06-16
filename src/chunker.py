import re


def split_text_into_chunks(text, chunk_size=1000, overlap=100):
    """
    Splits a long text into smaller chunks with overlap.

    Parameters:
    text (str): Full text to split.
    chunk_size (int): Maximum number of characters per chunk.
    overlap (int): Number of characters repeated between chunks.

    Returns:
    list: A list of text chunks.
    """

    if chunk_size <= overlap:
        raise ValueError("chunk_size must be greater than overlap")

    chunks = []
    start = 0

    while start < len(text):
        end = start + chunk_size
        chunk = text[start:end]
        chunks.append(chunk)

        start = end - overlap

    return chunks

def split_text_by_separator(text, separator="=" * 80):
    """
    Splits text into complete document blocks using a separator line.

    This is useful when the text contains repeated delimiters between documents.
    """

    raw_blocks = text.split(separator)

    chunks = []

    for block in raw_blocks:
        clean_block = block.strip()

        if clean_block:
            chunks.append(clean_block)

    return chunks


def split_text_by_document_pattern(text):
    """
    Splits text into document blocks using document headers like:
    DOCUMENTO 1
    DOCUMENTO 2
    DOCUMENTO 3
    """

    pattern = r"(DOCUMENTO\s+\d+)"

    parts = re.split(pattern, text)

    chunks = []

    for i in range(1, len(parts), 2):
        header = parts[i].strip()
        body = parts[i + 1].strip() if i + 1 < len(parts) else ""

        chunk = f"{header}\n{body}"

        if chunk.strip():
            chunks.append(chunk)

    return chunks

def auto_chunk_text(text):
    """
    Automatically selects the best chunking strategy based on document structure.

    Returns:
    tuple: (chunks, selected_strategy)
    """

    separator = "=" * 80
    document_pattern = r"DOCUMENTO\s+\d+"

    if separator in text:
        print("Auto strategy selected: separator")
        return split_text_by_separator(text), "separator"

    if re.search(document_pattern, text):
        print("Auto strategy selected: pattern")
        return split_text_by_document_pattern(text), "pattern"

    print("Auto strategy selected: overlap")
    return split_text_into_chunks(
        text=text,
        chunk_size=1000,
        overlap=100
    ), "overlap"