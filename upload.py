from langchain_community.document_loaders.csv_loader import CSVLoader
from langchain_qdrant import QdrantVectorStore
from langchain_ollama import OllamaEmbeddings  

embeddings = OllamaEmbeddings(model="llama3.2")



loader = CSVLoader("students.csv")

data = loader.load_and_split()
            ###print(data)

url = "ENTER YOUR QDRANT URL "  
api = "ENTER YOUR QDRANT API KEY"


drant = QdrantVectorStore.from_documents(
    data,
    embeddings,
    url=url,
    prefer_grpc=True,
    api_key=api,
    collection_name="dictionary",
)
