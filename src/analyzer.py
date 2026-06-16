import re


def extract_metadata_from_text(text):
    """
    Extracts basic structured information from a text block.

    Returns a dictionary with:
    - document_id
    - name
    - company
    - email
    - city
    """

    document_id = re.search(r"DOCUMENTO\s+(\d+)", text)
    name = re.search(r"Nombre:\s*(.+)", text)
    company = re.search(r"Empresa:\s*(.+)", text)
    email = re.search(r"Email:\s*([\w\.-]+@[\w\.-]+)", text)
    city = re.search(r"Ciudad:\s*(.+)", text)

    return {
        "document_id": document_id.group(1) if document_id else None,
        "name": name.group(1).strip() if name else None,
        "company": company.group(1).strip() if company else None,
        "email": email.group(1).strip() if email else None,
        "city": city.group(1).strip() if city else None,
    }