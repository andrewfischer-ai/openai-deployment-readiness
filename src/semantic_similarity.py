import math

from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

client = OpenAI()


def get_embedding(text):
    """Convert text into a numerical vector."""

    response = client.embeddings.create(
        model="text-embedding-3-small",
        input=text
    )

    return response.data[0].embedding


def cosine_similarity(vector_a, vector_b):
    """Calculate similarity between two vectors."""

    dot_product = sum(
        a * b for a, b in zip(vector_a, vector_b)
    )

    magnitude_a = math.sqrt(
        sum(a * a for a in vector_a)
    )

    magnitude_b = math.sqrt(
        sum(b * b for b in vector_b)
    )

    if magnitude_a == 0 or magnitude_b == 0:
        return 0.0

    return dot_product / (magnitude_a * magnitude_b)

if __name__ == "__main__":
     
    question_a = "Who approves large AI investments?"

    question_b = (
        "What authorization is required for major "
        "artificial intelligence expenditures?"
    )

    question_c = (
        "What cybersecurity procedures must be "
        "completed before deployment?"
    )


    embedding_a = get_embedding(question_a)
    embedding_b = get_embedding(question_b)
    embedding_c = get_embedding(question_c)


    similarity_ab = cosine_similarity(embedding_a, embedding_b)
    similarity_ac = cosine_similarity(embedding_a, embedding_c)


    print("\nSEMANTIC SIMILARITY ANALYSIS")
    print("----------------------------")

    print(f"A vs. B: {similarity_ab:.4f}")
    print(f"A vs. C: {similarity_ac:.4f}")
     
