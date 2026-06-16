import csv
from pathlib import Path

from analyzer import extract_metadata_from_text
from chunker import auto_chunk_text, split_text_by_separator, split_text_into_chunks
from file_loader import load_text_from_file
from reporter import save_strategy_report


class SmartDocumentAnalyzer:
    def __init__(
        self,
        input_file,
        expected_documents=1000,
        chunking_strategy="auto",
        output_folder="outputs/chunks",
        csv_output="outputs/extracted_metadata.csv",
    ):
        self.input_file = Path(input_file)
        self.expected_documents = expected_documents
        self.chunking_strategy = chunking_strategy
        self.output_folder = Path(output_folder)
        self.csv_output = Path(csv_output)

    def get_input_files(self):
        if self.input_file.is_file():
            return [self.input_file]

        if self.input_file.is_dir():
            supported_extensions = [".txt", ".pdf", ".docx"]

            files = []

            for file_path in self.input_file.iterdir():
                if file_path.suffix.lower() in supported_extensions:
                    files.append(file_path)

            return files

        raise FileNotFoundError(f"Input path not found: {self.input_file}")

    def load_text(self, file_path):
        return load_text_from_file(file_path)

    def create_chunks(self, text):
        selected_strategy = self.chunking_strategy

        if self.chunking_strategy == "separator":
            chunks = split_text_by_separator(text)

        elif self.chunking_strategy == "overlap":
            chunks = split_text_into_chunks(
                text=text,
                chunk_size=1000,
                overlap=100
            )

        elif self.chunking_strategy == "auto":
            chunks, selected_strategy = auto_chunk_text(text)

        else:
            raise ValueError(
                "Invalid chunking strategy. Use 'separator', 'overlap' or 'auto'."
            )

        return chunks, selected_strategy

    def extract_metadata(self, chunks, source_file):
        all_metadata = []

        for chunk in chunks:
            metadata = extract_metadata_from_text(chunk)

            if metadata["document_id"] is not None:
                metadata["source_file"] = source_file.name
                all_metadata.append(metadata)

        return all_metadata

    def calculate_metrics(self, total_characters, total_chunks, all_metadata):
        total_metadata_records = len(all_metadata)

        unique_document_ids = set()

        for record in all_metadata:
            unique_key = f"{record['source_file']}::{record['document_id']}"
            unique_document_ids.add(unique_key)

        unique_documents_found = len(unique_document_ids)
        duplicate_records = total_metadata_records - unique_documents_found

        extraction_rate = (total_metadata_records / self.expected_documents) * 100
        unique_extraction_rate = (
            unique_documents_found / self.expected_documents
        ) * 100

        return {
            "total_characters": total_characters,
            "total_chunks": total_chunks,
            "total_metadata_records": total_metadata_records,
            "unique_documents_found": unique_documents_found,
            "duplicate_records": duplicate_records,
            "extraction_rate": extraction_rate,
            "unique_extraction_rate": unique_extraction_rate,
        }

    def save_metadata_csv(self, all_metadata):
        with self.csv_output.open("w", newline="", encoding="utf-8") as file:
            writer = csv.DictWriter(
                file,
                fieldnames=[
                    "source_file",
                    "document_id",
                    "name",
                    "company",
                    "email",
                    "city",
                ],
            )

            writer.writeheader()
            writer.writerows(all_metadata)

        return self.csv_output

    def save_chunks(self, chunks, source_file):
        self.output_folder.mkdir(parents=True, exist_ok=True)

        source_name = source_file.stem

        for i, chunk in enumerate(chunks, start=1):
            chunk_file = self.output_folder / f"{source_name}_chunk_{i:03}.txt"
            chunk_file.write_text(chunk, encoding="utf-8")

    def run(self):
        input_files = self.get_input_files()

        all_metadata = []
        total_characters = 0
        total_chunks = 0
        selected_strategies = {}

        for file_path in input_files:
            print(f"\nProcessing file: {file_path}\n")

            text = self.load_text(file_path)

            chunks, selected_strategy = self.create_chunks(text)

            total_characters += len(text)
            total_chunks += len(chunks)
            selected_strategies[file_path.name] = selected_strategy

            print(f"Total characters in file: {len(text)}")
            print(f"Chunks created for file: {len(chunks)}")

            print("\nAnalyzing first chunk...\n")
            first_chunk_metadata = extract_metadata_from_text(chunks[0])
            print(first_chunk_metadata)

            file_metadata = self.extract_metadata(chunks, file_path)
            all_metadata.extend(file_metadata)

            self.save_chunks(chunks, file_path)

        metrics = self.calculate_metrics(total_characters, total_chunks, all_metadata)

        print(f"\nTotal files processed: {len(input_files)}")
        print(f"Total characters: {metrics['total_characters']}")
        print(f"Total chunks created: {metrics['total_chunks']}")
        print(f"Total metadata records extracted: {metrics['total_metadata_records']}")
        print(f"Unique documents found: {metrics['unique_documents_found']}")
        print(f"Duplicate records detected: {metrics['duplicate_records']}")
        print(f"Extraction rate: {metrics['extraction_rate']:.2f}%")
        print(f"Unique extraction rate: {metrics['unique_extraction_rate']:.2f}%")
        print(f"Chunking strategy requested: {self.chunking_strategy}")
        print(f"Chunking strategies selected: {selected_strategies}")

        report_file = save_strategy_report(
            requested_strategy=self.chunking_strategy,
            selected_strategy=str(selected_strategies),
            total_characters=metrics["total_characters"],
            total_chunks=metrics["total_chunks"],
            total_metadata_records=metrics["total_metadata_records"],
            unique_documents_found=metrics["unique_documents_found"],
            duplicate_records=metrics["duplicate_records"],
            extraction_rate=metrics["extraction_rate"],
            unique_extraction_rate=metrics["unique_extraction_rate"],
        )

        print(f"Strategy report saved to {report_file}")

        csv_file = self.save_metadata_csv(all_metadata)
        print(f"Metadata saved to {csv_file}")

        print("Chunks saved successfully.")