from qdrant_client import QdrantClient
from docling.chunking import HybridChunker
from docling.datamodel.base_models import InputFormat
from docling.document_converter import DocumentConverter
from langchain_text_splitters import CharacterTextSplitter


url = "Enter your url"  
api_key = "enter your api key"


client = QdrantClient(url=url, api_key=api_key)


client.set_model("sentence-transformers/all-MiniLM-L6-v2")
client.set_sparse_model("Qdrant/bm25")


def upload_pdf(file_path, collection_name):
  
    # Initialize document converter with supported formats
    doc_converter = DocumentConverter(
        allowed_formats=[
            InputFormat.PPTX,
            InputFormat.PDF,
            InputFormat.DOCX,
            InputFormat.XLSX,
          
        ]
    )

    # Convert document
    document = doc_converter.convert(file_path)

    # Process document chunks
    documents, metadatas = [], []
    text_splitter = CharacterTextSplitter(chunk_size=512, chunk_overlap=0)
    chunks = text_splitter.split_text(document.text)

    for chunk in chunks:
        documents.append(chunk)
        metadatas.append(document.meta.export_json_dict())

    # Upload to Qdrant
    qdrant = client.add(
        collection_name=collection_name,
        documents=documents,
        metadata=metadatas,
        batch_size=64
    )


upload_pdf("Indian-Recipes.pdf","indian-receipe")