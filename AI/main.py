from model import Model
from definition import Definition


prompt = """I have 2 sentences {first} and {second} 
extract me parts of sentences where they are different 
and when we suggest that first is correct what should I add/remove/fix globally in second sentence in form  To make the second sentence correct ....
and explain why in form Explanation: "explanation" """

solver = Model(prompt)
definer = Definition()

pdf_path1 = 'Ziadost_filled.pdf'
pdf_path2 = 'Ziadost_user.pdf'

definer.get_differences(pdf_path1, pdf_path2)

# print(definer.differences)

print(solver.handle_differences(definer.differences))


# for (first, second) in definer.differences:
#     res = solver.invoke(first, second).split("\n")

#     for i in res:
#         if "Explanation:" in i or "To make the second sentence correct" in i:
#             print(i)
#             print()



# first = "- Stavebník, meno a priezvisko (názov): Illia"
# second = "- Stavebník, meno a priezvisko (názov): Illia Volk"

# print(solver.invoke(first, second))