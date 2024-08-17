from src.helper import load_pdf, text_split, download_hugging_face_embeddings
from langchain.vectorstores import FAISS
from dotenv import load_dotenv
import os

load_dotenv()



# print(PINECONE_API_KEY)
# print(PINECONE_API_ENV)

extracted_data = load_pdf("data/")
text_chunks = text_split(extracted_data)
embeddings = download_hugging_face_embeddings()


#Initializing the Pinecone
faiss_db = FAISS.from_documents([t.page_content for t in text_chunks], embeddings)
