import json
from pathlib import Path


def save_strategy_report(
    requested_strategy,
    selected_strategy,
    total_characters,
    total_chunks,
    total_metadata_records,
    unique_documents_found,
    duplicate_records,
    extraction_rate,
    unique_extraction_rate,
    output_path="outputs/strategy_report.json"
):
    report = {
        "requested_strategy": requested_strategy,
        "selected_strategy": selected_strategy,
        "total_characters": total_characters,
        "total_chunks": total_chunks,
        "total_metadata_records": total_metadata_records,
        "unique_documents_found": unique_documents_found,
        "duplicate_records": duplicate_records,
        "extraction_rate": round(extraction_rate, 2),
        "unique_extraction_rate": round(unique_extraction_rate, 2),
    }

    output_file = Path(output_path)

    output_file.write_text(
        json.dumps(report, indent=4),
        encoding="utf-8"
    )

    return output_file