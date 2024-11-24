from .model import Model
from .definition import Definition
from base64 import b64decode
from .remake_to_pdf import string_to_pdf_with_colors


prompt = """
You should see how forms are filled correctly and keep structure of form and give me the answer is user's input correct or not and if not how to fix it
{context}
Given sequences of two sentences, where the first is correct: and the second potentially has errors, evaluate both.
when giving advices and suggestions think in context of grammar and context of sentence but it mustn't be exact copy of first sentence
Provide a correction for the second sentence in the format: "Change ..."
Include an explanation based on grammar rules, contextual clarity, and stylistic consistency without mentioning words "Second/first sentence": "Explanation: .... "
and give the answer in {language}
"""

solver = Model(prompt)
definer = Definition()


def correct_answer(item, filetype="pdf", language="english"):


    pdf_correct = 'templateFile.pdf'
    pdf_user = 'userFile.pdf'

    with open('userFile.pdf', 'wb') as fw:
        fw.write(b64decode(item["userFile"]))

    with open('templateFile.pdf', 'wb') as fw:
        fw.write(b64decode(item["templateFile"]))

    if filetype == "pdf":
        definer.get_pdf_differences(pdf_correct, pdf_user)
    
    definer.higlight_differences(definer.extract_text_from_pdf(pdf_user))
    string_to_pdf_with_colors(definer.highlighted_text)

    
    return solver.handle_differences(definer.differences, language), definer.highlighted_text



# pdf_correct = 'Ziadost_filled.pdf'
# pdf_user = 'Ziadost_user.pdf'
# definer.get_pdf_differences(pdf_correct, pdf_user)


# print(solver.invoke(definer.differences, "english").split('\n'))

# print(definer.differences)
