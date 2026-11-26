from pathlib import Path
import re


DOCUMENTS_DIR = Path(__file__).resolve().parent.parent / "documents"


def load_document(filename):
    """Read a text document from the documents directory."""

    file_path = DOCUMENTS_DIR / filename

    with open(file_path, "r", encoding="utf-8") as file:
        return file.read()


def split_into_sections(document_text):
    """Split a policy document at SECTION headings."""

    sections = re.split(
        r"(?=SECTION \d+ —)",
        document_text
    )

    chunks = []

    for section in sections:
        section = section.strip()

        if not section:
            continue

        chunks.append(section)

    return chunks


if __name__ == "__main__":

    document = load_document("ai_investment_policy.txt")

    chunks = split_into_sections(document)

    print(f"\nTotal document sections: {len(chunks)}")

    for number, chunk in enumerate(chunks, start=1):

        print(f"\n--- CHUNK {number} ---")
        print(chunk)
