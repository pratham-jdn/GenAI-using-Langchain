from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

load_dotenv()

chat_model = ChatOpenAI(model='gpt-4o', temperature=0.7)

chat_result = chat_model.invoke("What is the capital of India?")

print(chat_result.content)