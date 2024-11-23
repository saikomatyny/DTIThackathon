from dotenv import load_dotenv
import os
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
import json




class Model:
    def __init__(self, prompt) -> None:

        load_dotenv()
        model = ChatOpenAI(model="gpt-4o", api_key=os.getenv("OPENAI_API_KEY"), temperature=0.3)

        prompt_template = ChatPromptTemplate.from_messages(
            [("system", prompt)]
        )

        self.chain = prompt_template | model
        self.resposne = {}
    

    def invoke(self, first, second):
        response = self.chain.invoke({"first": first, "second": second})
        return response.content


    def answer(self, first, second):
        content = self.invoke(first, second)
        answer_json = {}

        res = content.split("\n")
        for sentence in res:

            if "To make the second sentence correct" in sentence:
                answer_json["correct"] = sentence
            
            if "Explanation:" in sentence:
                answer_json["explanation"] = sentence
        
        return answer_json
    

    def handle_differences(self, differences):
        answers = []
        for (first, second) in differences:
            answers.append(self.answer(first, second))
        
        
        json_string = json.dumps(answers, indent=4)

        return json_string
        


            

        





        


        