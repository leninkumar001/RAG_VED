from langchain_ollama import OllamaEmbeddings
from langchain_qdrant import QdrantVectorStore
from llm import *

embeddings = OllamaEmbeddings(model="llama3.2:latest")

qdrant_url = "https://60750fe2-661a-4258-90c2-721288c91c85.us-east4-0.gcp.cloud.qdrant.io:6333"
qdrant_api_key = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJhY2Nlc3MiOiJtIn0.h_O2Mf5zsKjlCFQiue_Bw8EwqB5hK6AmzrfcAnAZmYA"

question = input("Enter your question: ")

qdrant = QdrantVectorStore.from_existing_collection(
    embedding=embeddings,
    url=qdrant_url,
    api_key=qdrant_api_key,
    collection_name="my_documents",
)

response =  qdrant.similarity_search(
    query=question,
    k=5)
# for score in response:
#     print(  score)

prompt = f"""

Question: {question},
context: {response}
Only return the summary based on the provided content.
"""

print(completion_llm(prompt))
# for i in completion_llm(prompt):
#     print(i, end="", flush=True)