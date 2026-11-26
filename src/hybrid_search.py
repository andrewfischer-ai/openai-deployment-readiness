from dotenv import load_dotenv
from openai import OpenAI

from src.document_loader import load_document, split_into_sections
from src.retrieval import search_documents
from src.semantic_similarity import cosine_similarity
from src.embedding_cache import get_cached_embedding

load_dotenv()

client = OpenAI()


def hybrid_search(question, chunks, top_k=3):

    # Generate the question embedding
    question_embedding = get_cached_embedding(question)

    # Retrieve keyword matches
    keyword_results = search_documents(
        question,
        chunks,
        top_k=len(chunks)
    )

    keyword_scores = {
        result["content"]: result["score"]
        for result in keyword_results
    }

    results = []

    for chunk in chunks:

        # Generate a semantic embedding
        chunk_embedding = get_cached_embedding(chunk)

        # Calculate semantic similarity
        semantic_score = cosine_similarity(
            question_embedding,
            chunk_embedding
        )

        # Retrieve keyword score
        keyword_score = keyword_scores.get(chunk, 0)

        # Normalize keyword score to a 0–1 scale
        normalized_keyword_score = min(keyword_score / 5, 1.0)

        # Combine retrieval scores
        combined_score = (
            0.2 * normalized_keyword_score
            + 0.8 * semantic_score
        )

        results.append({
            "keyword_score": keyword_score,
            "semantic_score": semantic_score,
            "combined_score": combined_score,
            "content": chunk
        })

    results.sort(
        key=lambda result: result["combined_score"],
        reverse=True
    )

    return results[:top_k]


if __name__ == "__main__":

    document = load_document("ai_investment_policy.txt")
    chunks = split_into_sections(document)

    question = (
        "Who authorizes major expenditures "
        "for artificial intelligence projects?"
    )

    results = hybrid_search(question, chunks, top_k=5)

    print("\nHYBRID SEARCH RESULTS")
    print("---------------------")

    for result in results:

        print(f"\nKeyword score: {result['keyword_score']}")
        print(f"Semantic score: {result['semantic_score']:.4f}")
        print(f"Combined score: {result['combined_score']:.4f}")

        print(result["content"][:300])
