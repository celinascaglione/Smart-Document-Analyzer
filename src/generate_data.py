from faker import Faker

fake = Faker()

NUMBER_OF_DOCUMENTS = 1000
USE_SEPARATOR = False
OUTPUT_FORMAT = "txt"


def get_output_file():
    """
    Returns the appropriate output file based on the selected format.
    """

    if OUTPUT_FORMAT == "txt":
        return "data/sample_without_separator.txt"

    elif OUTPUT_FORMAT == "docx":
        return "data/sample_without_separator.docx"

    elif OUTPUT_FORMAT == "pdf":
        return "data/sample_without_separator.pdf"

    else:
        raise ValueError("Unsupported output format.")


def generate_dataset():
    """
    Generates a synthetic dataset in text format.

    NOTE:
    For now, only TXT generation is implemented.
    DOCX and PDF support will be added in future versions.
    """

    if OUTPUT_FORMAT != "txt":
        raise NotImplementedError(
            "DOCX and PDF generation are not implemented yet."
        )

    output_file = get_output_file()

    with open(output_file, "w", encoding="utf-8") as f:

        for i in range(NUMBER_OF_DOCUMENTS):

            f.write(f"DOCUMENTO {i + 1}\n")
            f.write(f"Nombre: {fake.name()}\n")
            f.write(f"Empresa: {fake.company()}\n")
            f.write(f"Email: {fake.email()}\n")
            f.write(f"Ciudad: {fake.city()}\n")
            f.write(fake.text(max_nb_chars=1200))
            f.write("\n")

            if USE_SEPARATOR:
                f.write("=" * 80)
                f.write("\n\n")
            else:
                f.write("\n\n")

    print(f"Dataset generated successfully: {output_file}")


if __name__ == "__main__":
    generate_dataset()