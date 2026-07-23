from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv

load_dotenv()

embeddings_model = OpenAIEmbeddings(model='text-embedding-3-large', dimensions=32)

embedding_result = embeddings_model.embed_query("Delhi is the capital of India")

print(str(embedding_result))