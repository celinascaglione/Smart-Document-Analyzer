from smart_analyzer import SmartDocumentAnalyzer


INPUT_FILE = "documents"

CHUNKING_STRATEGY = "auto"

EXTRACTION_MODE = "regex"
# Cambiar a "llm" para usar OpenAI

EXPECTED_DOCUMENTS = 3000


def main():
    analyzer = SmartDocumentAnalyzer(
        input_file=INPUT_FILE,
        expected_documents=EXPECTED_DOCUMENTS,
        chunking_strategy=CHUNKING_STRATEGY,
        extraction_mode=EXTRACTION_MODE,
    )

    analyzer.run()


if __name__ == "__main__":
    main()