from model import Model
from definition import Definition


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


def correct_answer(filetype="pdf", language="english"):

    pdf_correct = 'Ziadost_filled.pdf'
    pdf_user = 'Ziadost_user.pdf'

    if filetype == "pdf":
        definer.get_pdf_differences(pdf_correct, pdf_user)
    
    return solver.handle_differences(definer.differences, language)


print(correct_answer())

# pdf_correct = 'Ziadost_filled.pdf'
# pdf_user = 'Ziadost_user.pdf'
# definer.get_pdf_differences(pdf_correct, pdf_user)


# print(solver.invoke(definer.differences, "english").split('\n'))

# print(definer.differences)