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
    

    def invoke(self, first, second, language):
        response = self.chain.invoke({"first": first, "second": second, "language": language})
        return response.content


    def answer(self, first, second, language):
        content = self.invoke(first, second, language)
        answer_json = {}

        res = content.split("\n")
        for sentence in res:

            if "To make the second sentence correct" in sentence:
                answer_json["correct"] = sentence
            
            if "Explanation:" in sentence:
                answer_json["explanation"] = sentence
        
        return answer_json
    

    def handle_differences(self, differences, language):
        answers = []
        for (first, second) in differences:
            answers.append(self.answer(first, second, language))
        
        
        json_string = json.dumps(answers, indent=4)

        return json_string
        


            

        





        


        