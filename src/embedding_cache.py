import hashlib
import json
from pathlib import Path

from dotenv import load_dotenv
from openai import OpenAI


load_dotenv()

client = OpenAI()

MODEL = "text-embedding-3-small"

CACHE_DIR = Path(__file__).resolve().parent.parent / "cache"
CACHE_DIR.mkdir(exist_ok=True)

CACHE_FILE = CACHE_DIR / "embeddings.json"


def get_cached_embedding(text):
    """Retrieve an embedding from cache or generate a new one."""

    # Create a unique identifier for the model and text
    cache_key = hashlib.sha256(
        f"{MODEL}:{text}".encode("utf-8")
    ).hexdigest()

    # Load the existing cache
    if CACHE_FILE.exists():
        with open(CACHE_FILE, "r", encoding="utf-8") as file:
            cache = json.load(file)
    else:
        cache = {}

    # Check whether the embedding already exists
    if cache_key in cache:
        print("CACHE HIT: Reusing stored embedding")
        return cache[cache_key]

    # Generate a new embedding
    print("CACHE MISS: Calling OpenAI API")

    response = client.embeddings.create(
        model=MODEL,
        input=text
    )

    embedding = response.data[0].embedding

    # Save the new embedding
    cache[cache_key] = embedding

    with open(CACHE_FILE, "w", encoding="utf-8") as file:
        json.dump(cache, file)

    return embedding


if __name__ == "__main__":

    text = "Who approves large AI investments?"

    embedding = get_cached_embedding(text)

    print(f"Embedding dimensions: {len(embedding)}")
    
