from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

client = OpenAI()

text = "Who approves large AI investments?"

response = client.embeddings.create(
    model="text-embedding-3-small",
    input=text
)

embedding = response.data[0].embedding

print("\nEMBEDDING EXAMPLE")
print("-----------------")

print(f"Original text: {text}")
print(f"Vector dimensions: {len(embedding)}")
print(f"First 10 values: {embedding[:10]}")
