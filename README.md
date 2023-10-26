
# LangChain_with_Pinecone

In this project, we will learn how to use PineCone.
using Langchain and how to use chat with your data

## Installation

These are the required packages

* Langchain
* OpenAI
* Pinecone-Client 

## Documentation


Here, we are going to see how to store the user data. (text data) into vector stores and use RetrievalQA to ask questions about that data.


We have taken a text file that contains Wekepidia foldable phone information. Then we passed this text data into a text splitter with a chunk size of 1000. and we took embeddings and model from OpenAI.


For the vector database, we chose Pinecone, where we passed chunked text and OpenAI embeddings to change into a vector and store it. then using RetrievalQA to query the questions.


## Features

* Model -- OpenAI API
* Embeddings -- OpenAI API
* Text splitter -- CharacterTextSplitter
* Vector DB -- Pinecone
* QA chain -- qa_retriable


## Authors

- [@sasidhar](https://github.com/sastrysasi4)

