#load existing index
from dotenv import load_dotenv
import os
from pinecone import Pinecone
from src.helper import load_pdf_files,filter_to_minimal_docs,download_embeddings,text_split
from langchain_pinecone import PineconeVectorStore
from pinecone import ServerlessSpec

load_dotenv()

PINECONE_API_KEY =os.environ.get("PINECONE_API_KEY")
GROQ_API_KEY=os.environ.get("GROQ_API_KEY")

os.environ["GROQ_API_KEY"] = GROQ_API_KEY
os.environ["PINECONE_API_KEY"] = PINECONE_API_KEY

extracted_data= load_pdf_files(data='data/')
filter_data = filter_to_minimal_docs(extracted_data)
texts_chunk = text_split(filter_data)

#embed each chunk and upsert the embeddings into your Pinecone index

print("Loading embeddings model... (this may take a few minutes on first run)")
embeddings = download_embeddings()
print("Embeddings loaded successfully!")

pinecone_api_key = PINECONE_API_KEY
pc = Pinecone(api_key=pinecone_api_key)

index_name = "medical-chatbot"

if not pc.has_index(index_name):
    pc.create_index(
        name = index_name,
        dimension=384,
        metric = "cosine",
        spec=ServerlessSpec(cloud="aws",region="us-east-1")
        
    )
index = pc.Index(index_name)

docsearch = PineconeVectorStore.from_documents(
    documents=texts_chunk,
    embedding=embeddings,
    index_name=index_name,
) 