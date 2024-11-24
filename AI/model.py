from dotenv import load_dotenv
import os
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
import json
from langchain_community.document_loaders import PyPDFLoader
from langchain_core.vectorstores import InMemoryVectorStore
from langchain_openai import OpenAIEmbeddings
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain.chains import create_retrieval_chain
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain_core.prompts import ChatPromptTemplate





class Model:
    def __init__(self, prompt, temperature=0.3) -> None:

        load_dotenv()
        model = ChatOpenAI(model="gpt-4o", api_key=os.getenv("OPENAI_API_KEY"), temperature=temperature)

        file_path = os.path.join("AI", "dataset", "1.pdf");
        loader = PyPDFLoader(file_path)

        docs = loader.load()

        text_splitter = RecursiveCharacterTextSplitter(chunk_size=50, chunk_overlap=10)
        splits = text_splitter.split_documents(docs)
        vectorstore = InMemoryVectorStore.from_documents(
            documents=splits, embedding=OpenAIEmbeddings()
        )

        retriever = vectorstore.as_retriever()

        prompt = ChatPromptTemplate.from_messages(
            [
                ("system", prompt),
                ("human", "{input}"),
            ]
        )

        question_answer_chain = create_stuff_documents_chain(model, prompt)
        rag_chain = create_retrieval_chain(retriever, question_answer_chain)

        self.chain = rag_chain
        self.resposne = {}
    

    def invoke(self, sentences, language):
        response = self.chain.invoke({"input": sentences, "language": language})
        return response["answer"]

    

    def handle_differences(self, differences, language):
        answer = self.invoke(differences, language).split('\n')
        filtered_answer = [element for element in answer if element != '']
        final_answers = []

        print(filtered_answer)



        for i in range(0, len(filtered_answer), 2):
            final_answers.append({"correct": filtered_answer[i], "explanation": filtered_answer[i+1]})
        
        json_string = json.dumps(final_answers, indent=4)

        return json_string
        


            

        





        


        
