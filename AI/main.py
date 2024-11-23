from model import Model
from definition import Definition


prompt = """
Given two sentences, where the first is correct: "{first}" and the second potentially has errors: "{second}", evaluate both.
If the second sentence deviates from the correctness of the first in meaning, grammar, or style, suggest necessary corrections.
Provide a correction in the format: "To make the second sentence correct ..."
Include an explanation based on grammar rules, contextual clarity, and stylistic consistency: "Explanation: ...."
"""

solver = Model(prompt)
definer = Definition()


def correct_answer(filetype="pdf", language="english"):

    pdf_correct = 'templateFile.pdf'
    pdf_user = 'userFile.pdf'

    definer.get_differences(pdf_correct, pdf_user)

    return solver.handle_differences(definer.differences)


