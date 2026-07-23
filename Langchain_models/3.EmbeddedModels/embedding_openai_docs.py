from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv

load_dotenv()

embeddings_model = OpenAIEmbeddings(model='text-embedding-3-large', dimensions=32)

documents = [
    "Delhi is the capital of India",
    "Mumbai is the financial capital of India",
    "Kolkata is the cultural capital of India"
]

embedding_result = embeddings_model.embed_documents(documents)

print(str(embedding_result))