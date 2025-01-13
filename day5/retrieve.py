from qdrant_client import QdrantClient

from docling.chunking import HybridChunker
from docling.datamodel.base_models import InputFormat
from docling.document_converter import DocumentConverter

# ## url and api key qdrant 
url = "enter your url"  
api_key = "enter your api key"



doc_converter = DocumentConverter(allowed_formats=[InputFormat.PDF])
client = QdrantClient(url=url,api_key=api_key)



client.set_model("sentence-transformers/all-MiniLM-L6-v2")
client.set_sparse_model("Qdrant/bm25")


result = doc_converter.convert(
    "docklinglaws.pdf"
)


documents, metadatas = [], []
for chunk in HybridChunker().chunk(result.document):
    documents.append(chunk.text)
    metadatas.append(chunk.meta.export_json_dict())

qdrant = client.add(
    collection_name="Pdfdockling",
    documents=documents,
    metadata=metadatas,
    batch_size=64,
)