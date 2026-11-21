from dotenv import load_dotenv
from openai import OpenAI

# Load variables stored in the .env file
load_dotenv()

# Create a client that authenticates using OPENAI_API_KEY
client = OpenAI()

# Send a request to an OpenAI model
response = client.responses.create(
    model="gpt-6-luna",
    input="Explain in two sentences what an API is to an aerospace engineer."
)

# Print the model's text response
print(response.output_text)
