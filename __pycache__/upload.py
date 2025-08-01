from langchain_community.document_loaders import PyPDFLoader
from langchain_qdrant import QdrantVectorStore
from langchain_ollama import OllamaEmbeddings


# Add Qdrant client import
from qdrant_client import QdrantClient

# File Load and Chunk
file_path = r"C:\Users\CSESTUDENT\Desktop\krishna\bitcoin.pdf"
loader = PyPDFLoader(file_path)
docs = loader.load_and_split() 

# Display chunking information
print(f"Total number of chunks: {len(docs)}")
for i, doc in enumerate(docs):
    print(f"\n--- Chunk {i+1} 💹 ---")
    # print(doc.page_content[:500])  # Display first 500 characters of each chunk

embeddings = OllamaEmbeddings(
    model="llama3.2:latest",
)

qdrant_url = "https://60750fe2-661a-4258-90c2-721288c91c85.us-east4-0.gcp.cloud.qdrant.io:6333"
qdrant_api_key = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJhY2Nlc3MiOiJtIn0.h_O2Mf5zsKjlCFQiue_Bw8EwqB5hK6AmzrfcAnAZmYA"

# Create Qdrant client
qdrant_client = QdrantClient(
    url=qdrant_url,
    api_key=qdrant_api_key,
)

# Using Qdrant vector store from langchain_community with client
qdrant = QdrantVectorStore.from_documents(
    docs,
    embeddings,
    url= qdrant_url,
    api_key= qdrant_api_key,
    prefer_grpc=True,
    collection_name="my_documents",
)