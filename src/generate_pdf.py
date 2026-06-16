from pathlib import Path
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas


INPUT_FILE = "data/sample.txt"
OUTPUT_FILE = "data/sample.pdf"


def generate_pdf_from_txt():
    input_file = Path(INPUT_FILE)
    output_file = Path(OUTPUT_FILE)

    text = input_file.read_text(encoding="utf-8")

    pdf = canvas.Canvas(str(output_file), pagesize=letter)
    width, height = letter

    x = 40
    y = height - 40
    line_height = 12

    for line in text.splitlines():
        if y < 40:
            pdf.showPage()
            y = height - 40

        pdf.drawString(x, y, line[:100])
        y -= line_height

    pdf.save()

    print(f"PDF generated successfully: {output_file}")


if __name__ == "__main__":
    generate_pdf_from_txt()