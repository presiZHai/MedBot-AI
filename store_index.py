from src.helper import load_pdf, split_text, download_HugginFace_embeddings
from pinecone import Pinecone, ServerlessSpec
from langchain_pinecone import PineconeVectorStore
from dotenv import load_dotenv
import os

load_dotenv()

api_key = os.getenv("PINECONE_API_KEY")

data_extract = load_pdf("data/")
text_chunks = split_text(data_extract)
embeddings = download_HugginFace_embeddings()

# Initialize the Pinecone client
pc = Pinecone(api_key=api_key)

index_name = "medbot"

if index_name not in pc.list_indexes().names():
    pc.create_index(
        name=index_name,
        dimension=384, 
        metric="cosine", 
        spec=ServerlessSpec(
            cloud="aws", 
            region="us-east-1"
        ) 
    ) 

# Create embeddings for each of the text chunks and upload to Pinecone
#Embed each chunk and upsert the embeddings into a distinct namespace called wondervector5000
namespace = "wondervector5000"

docsearch = PineconeVectorStore.from_documents(
    documents=text_chunks,
    index_name=index_name,
    embedding=embeddings, 
    namespace=namespace
)