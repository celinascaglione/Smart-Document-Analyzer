# Smart Document Analyzer for LLMs

## Overview

Smart Document Analyzer is a Python project designed to process large document collections and extract structured metadata from semi-structured text.

It supports TXT, DOCX, and PDF files, applies adaptive chunking strategies, extracts metadata using regular expressions, and exports results to CSV and JSON reports.

---

## Main Features

* Process a single file or a full folder of documents.
* Supports `.txt`, `.docx`, and `.pdf`.
* Automatically selects the best chunking strategy.
* Chunking strategies:

  * Separator-based chunking.
  * Pattern-based chunking.
  * Fixed-size overlap chunking.
* Extracts structured metadata:

  * document ID
  * name
  * company
  * email
  * city
  * source file
* Exports metadata to CSV.
* Generates execution reports in JSON.
* Detects duplicate records.
* Calculates extraction metrics.

---

## Current Test Results

The analyzer was tested on a folder containing:

* `sample.txt`
* `sample.docx`
* `sample.pdf`

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

Automatic strategies selected:

```text
sample.docx -> pattern
sample.pdf  -> separator
sample.txt  -> separator
```

---

## Project Structure

```text
Smart-Document-Analyzer/
│
├── data/
├── documents/
├── outputs/
│   ├── chunks/
│   ├── extracted_metadata.csv
│   └── strategy_report.json
│
├── src/
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
├── README.md
├── requirements.txt
└── .gitignore
```

---

## Technologies

* Python
* Faker
* pypdf
* python-docx
* reportlab
* Regular Expressions
* CSV
* JSON

---

## Future Improvements

* LLM-based extraction.
* Semantic chunking with embeddings.
* OCR support for scanned PDFs.
* Batch processing reports by file.
* Command-line interface.
* RAG-ready document pipeline.

---

## Author

Developed as a portfolio project focused on document processing pipelines for Large Language Models.
