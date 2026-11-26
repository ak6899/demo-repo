import streamlit as st
from PyPDF2 import PdfReader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_openai import OpenAIEmbeddings, ChatOpenAI
from langchain_community.vectorstores import FAISS
from langchain.chains.question_answering import load_qa_chain

from dotenv import load_dotenv
load_dotenv()
import os
my_api_key=os.get_env("OPENAI_API_KEY")

st.header("StudyBot")

with st.sidebar:
    st.title("My Notes")
    file=st.file_uploader("Upload your notes", type=["txt", "pdf", "docx"])
    
#Extracting file text from the uploaded file

if file is not None:
   my_pdf=PdfReader(file)
   text=""
   for page in my_pdf.pages:
        text+=page.extract_text()
   st.write(text)
        
# BREAK INTO CHUNKS

   splitter=RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=100, length_function=len)
   chunks=splitter.split_text(text)
   st.write(chunks)

# GENERATE EMBEDDINGS

   embeddings=OpenAIEmbeddings(api_key=my_api_key)
  
#Create a vector store and store embeddings into it  
   
   vector_store=FAISS.from_texts(chunks, embeddings)
   
   
#GETTING USER QUERY
   
   user_query=st.text_input("type your query here ")
   
#perform similarity search and fetch matching chunks

   matching_chunks=vector_store.similarity_search(user_query)
   
#Define our LLM

   llm=ChatOpenAI(
       api_key=my_api_key,
       model="gpt-4o-mini",
       temparature=0,
       max_tokens=200 
   )
   
   chain=load_qa_chain=load_qa_chain(llm, chain_type="stuff") 
   
   output=chain.run(input_documents=matching_chunks, question=user_query)
   
   st.write(output)