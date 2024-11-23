from dotenv import load_dotenv
import os
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
import json




class Model:
    def __init__(self, prompt, temperature=0.3) -> None:

        load_dotenv()
        model = ChatOpenAI(model="gpt-4o", api_key=os.getenv("OPENAI_API_KEY"), temperature=temperature)

        prompt_template = ChatPromptTemplate.from_messages(
            [("system", prompt)]
        )

        self.chain = prompt_template | model
        self.resposne = {}
    

    def invoke(self, sentences, language):
        response = self.chain.invoke({"sentences": sentences, "language": language})
        return response.content

    

    def handle_differences(self, differences, language):
        answer = self.invoke(differences, language).split('\n')
        filtered_answer = [element for element in answer if element != '']
        final_answers = []



        for i in range(0, len(filtered_answer), 2):
            final_answers.append({"correct": filtered_answer[i], "explanation": filtered_answer[i+1]})
        
        json_string = json.dumps(final_answers, indent=4)

        return json_string
        


            

        





        


        