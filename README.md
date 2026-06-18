# Smart Document Analyzer for LLMs

## Overview

**Smart Document Analyzer** is a Python project designed to process large collections of semi-structured documents and automatically extract structured metadata.

The application supports **TXT**, **DOCX**, and **PDF** files, applies adaptive chunking strategies, processes individual files or entire folders, and exports structured results to CSV and JSON reports.

The project was designed with a modular architecture that allows different extraction engines (Regex, OpenAI, and future LLMs) to be integrated without modifying the core analyzer.

---

# Features

* Process a single document or an entire folder.
* Support for:

  * `.txt`
  * `.docx`
  * `.pdf`
* Automatic chunking strategy selection.
* Multiple chunking strategies:

  * Separator-based
  * Pattern-based
  * Fixed-size overlap
* Metadata extraction:

  * document ID
  * name
  * company
  * email
  * city
  * source file
* CSV export.
* JSON execution reports.
* Duplicate detection.
* Extraction metrics.
* Command-line interface (CLI).
* Extensible extraction architecture using the Factory Pattern.
* Ready for OpenAI integration.

---

# Example CLI Usage

Run with default parameters:

```bash
python src/main.py
```

Run specifying options:

```bash
python src/main.py --input documents --chunking auto --extractor regex --expected 3000
```

Display help:

```bash
python src/main.py --help
```

---

# Current Test Results

The analyzer was tested using:

* sample.txt
* sample.docx
* sample.pdf

Results:

```text
Total files processed: 3
Total chunks created: 3000
Total metadata records extracted: 3000
Unique documents found: 3000
Duplicate records detected: 0
Extraction rate: 100.00%
Unique extraction rate: 100.00%
```

Automatic strategy selection:

```text
sample.docx -> pattern
sample.pdf  -> separator
sample.txt  -> separator
```

---

# Automated Tests

The project includes automated tests built with **pytest**.

Run them with:

```bash
set PYTHONPATH=src
pytest
```

Current status:

```text
7 passed
```

---

# Architecture

The extraction pipeline follows a Factory Pattern.

```text
                 SmartDocumentAnalyzer
                           │
                           ▼
                  ExtractorFactory
                    ┌───────────────┐
                    │               │
                    ▼               ▼
            RegexExtractor   OpenAIExtractor
```

This design makes it easy to add future extractors (Gemini, Ollama, Claude, etc.) without changing the analyzer itself.

---

# Project Structure

```text
Smart-Document-Analyzer/

├── data/
├── documents/
├── outputs/
│   ├── chunks/
│   ├── extracted_metadata.csv
│   └── strategy_report.json
│
├── src/
│   ├── extractors/
│   ├── analyzer.py
│   ├── chunker.py
│   ├── file_loader.py
│   ├── generate_data.py
│   ├── generate_docx.py
│   ├── generate_pdf.py
│   ├── reporter.py
│   ├── smart_analyzer.py
│   └── main.py
│
├── tests/
│   ├── test_chunker.py
│   ├── test_factory.py
│   ├── test_file_loader.py
│   └── test_regex_extractor.py
│
├── README.md
├── LICENSE
├── requirements.txt
└── .gitignore
```

---

# Technologies

* Python
* argparse
* pytest
* Faker
* pypdf
* python-docx
* reportlab
* Regular Expressions
* CSV
* JSON
## Screenshots

### Command Line Help

![CLI Help](images/cli_help.png)

### Execution Example

![Execution Example](images/execution.png)

### Automated Tests

![Pytest Results](images/tests.png)


---

# Future Improvements

* Real OpenAI-powered metadata extraction.
* Gemini integration.
* Ollama integration.
* OCR support for scanned PDFs.
* Semantic chunking using embeddings.
* RAG-ready document retrieval pipeline.
* Streamlit web interface.

---

# Author

Developed as a portfolio project focused on document processing pipelines and scalable architectures for Large Language Models (LLMs).
