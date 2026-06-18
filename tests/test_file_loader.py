from pathlib import Path

from file_loader import load_text_from_file

def test_load_text_from_txt_file(tmp_path):
    file_path = tmp_path / "sample.txt"
    file_path.write_text("Hello world", encoding="utf-8")

    text = load_text_from_file(file_path)

    assert text == "Hello world"


def test_file_loader_rejects_unsupported_file(tmp_path):
    file_path = tmp_path / "sample.xlsx"
    file_path.write_text("Unsupported", encoding="utf-8")

    try:
        load_text_from_file(file_path)
        assert False
    except ValueError:
        assert True