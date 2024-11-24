from .model import Model
from .definition import Definition
from base64 import b64decode


prompt = """
{sentences}
Given sequences of two sentences, where the first is correct: and the second potentially has errors, evaluate both.
If the second sentence deviates from the correctness of the first in meaning, grammar, or style, suggest necessary corrections.
Provide a correction in the format: "To make the second sentence correct ..."
Include an explanation based on grammar rules, contextual clarity, and stylistic consistency: "Explanation: .... "
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
    
    return solver.handle_differences(definer.differences, language), definer.highlighted_text



# pdf_correct = 'Ziadost_filled.pdf'
# pdf_user = 'Ziadost_user.pdf'
# definer.get_pdf_differences(pdf_correct, pdf_user)


# print(solver.invoke(definer.differences, "english").split('\n'))

# print(definer.differences)