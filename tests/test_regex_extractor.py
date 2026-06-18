from extractors.regex_extractor import RegexExtractor


def test_regex_extractor_returns_metadata():
    text = """
DOCUMENTO 1
Nombre: John Doe
Empresa: OpenAI
Email: john@example.com
Ciudad: San Francisco
"""

    extractor = RegexExtractor()
    metadata = extractor.extract(text)

    assert metadata["document_id"] == "1"
    assert metadata["name"] == "John Doe"
    assert metadata["company"] == "OpenAI"
    assert metadata["email"] == "john@example.com"
    assert metadata["city"] == "San Francisco"