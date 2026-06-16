from pathlib import Path
from pypdf import PdfReader
from docx import Document


def load_text_from_file(file_path):
    file_path = Path(file_path)
    suffix = file_path.suffix.lower()

    if suffix == ".txt":
        return file_path.read_text(encoding="utf-8")

    if suffix == ".pdf":
        reader = PdfReader(file_path)
        text = ""

        for page in reader.pages:
            page_text = page.extract_text()
            if page_text:
                text += page_text + "\n"

        return text

    if suffix == ".docx":
        document = Document(file_path)
        paragraphs = []

        for paragraph in document.paragraphs:
            paragraphs.append(paragraph.text)

        return "\n".join(paragraphs)

    raise ValueError(
        "Unsupported file type. Please use .txt, .pdf, or .docx"
    )