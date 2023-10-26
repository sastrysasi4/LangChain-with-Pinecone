from langchain.document_loaders import TextLoader
from langchain.text_splitter import CharacterTextSplitter
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.chains import RetrievalQA
from langchain.llms.openai import OpenAI
from langchain.vectorstores.pinecone import Pinecone
import pinecone

import os
from dotenv import load_dotenv
load_dotenv()

pinecone.init(      
	api_key=str(os.getenv('Pinecone_api')),      
	environment='gcp-starter'      
)      


if __name__ == '__main__':
    print('Hello vectorstore!')
    loader = TextLoader('my_data.txt')
    documents = loader.load()
    # print(documents)
    # print(len(documents))

    text_splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=0)
    texts = text_splitter.split_documents(documents)
    # print(len(texts))
    

    embeddings = OpenAIEmbeddings(openai_api_key = (os.getenv('OPENAI_API_KEY')))
    docsearch = Pinecone.from_documents(texts,embeddings,index_name='langchain-learning')

    qa_retriable = RetrievalQA.from_chain_type(
        llm=OpenAI(), 
        chain_type="stuff", 
        retriever=docsearch.as_retriever(), #search_kwargs={'k': 2}
        return_source_documents = True
    )
    query = "what is a foldable phone?"
 
    result = qa_retriable({ "query": query })
    print(result)
