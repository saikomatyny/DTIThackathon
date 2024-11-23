


prompt = """
Given two sentences, where the first is correct: "{first}" and the second potentially has errors: "{second}", evaluate both.
If the second sentence deviates from the correctness of the first in meaning, grammar, or style, suggest necessary corrections.
Provide a correction in the format: "To make the second sentence correct, {correction_action}."
Include an explanation based on grammar rules, contextual clarity, and stylistic consistency: "Explanation: '{reason}'"
"""