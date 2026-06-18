import argparse

from smart_analyzer import SmartDocumentAnalyzer


def parse_arguments():
    parser = argparse.ArgumentParser(
        description="Smart Document Analyzer"
    )

    parser.add_argument(
        "--input",
        default="documents",
        help="Input file or directory"
    )

    parser.add_argument(
        "--chunking",
        default="auto",
        choices=["auto", "separator", "pattern", "overlap"],
        help="Chunking strategy"
    )

    parser.add_argument(
        "--extractor",
        default="regex",
        choices=["regex", "openai"],
        help="Extraction mode"
    )

    parser.add_argument(
        "--expected",
        default=3000,
        type=int,
        help="Expected number of documents"
    )

    return parser.parse_args()


def main():
    args = parse_arguments()

    analyzer = SmartDocumentAnalyzer(
        input_file=args.input,
        expected_documents=args.expected,
        chunking_strategy=args.chunking,
        extraction_mode=args.extractor,
    )

    analyzer.run()


if __name__ == "__main__":
    main()