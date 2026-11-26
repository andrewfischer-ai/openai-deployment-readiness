import re

from src.document_loader import load_document, split_into_sections


def tokenize(text):
    """Convert text into a list of searchable words."""

    return re.findall(r"\b\w+\b", text.lower())


def search_documents(question, chunks, top_k=2):
    """Rank document chunks by shared keywords."""

    question_words = set(tokenize(question))

    results = []

    for chunk in chunks:

        chunk_words = set(tokenize(chunk))

        # Count the words shared by the question and chunk
        score = len(question_words.intersection(chunk_words))

        if score > 0:
            results.append({
                "score": score,
                "content": chunk
            })

    # Sort from highest to lowest relevance score
    results.sort(key=lambda result: result["score"], reverse=True)

    return results[:top_k]


if __name__ == "__main__":

    document = load_document("ai_investment_policy.txt")

    chunks = split_into_sections(document)

    question = "What approval is required for a $150,000 AI investment?"

    results = search_documents(question, chunks)

    print(f"\nQUESTION: {question}")

    for result in results:
        print(f"\nRELEVANCE SCORE: {result['score']}")
        print(result["content"])

