import pdfplumber


class Definition:

    def __init__(self) -> None:
        self.differences = ""
        self.highlighted_text = ""
        self.list_of_differences = []

    def extract_text_from_pdf(self, path):
        text = ''
        with pdfplumber.open(path) as pdf:
            for page in pdf.pages:
                text += page.extract_text() + '\n'
        return text

    def compare_texts(self, text1, text2):

        lines1 = text1.split('\n')
        lines2 = text2.split('\n')

        i = 0
        for line1, line2 in zip(lines1, lines2):
            if line1 != line2:
                self.differences+=f"First sentence: {line1}\nSecond sentence: {line2}\n"
                self.list_of_differences.append(i)
            i += 1

    def higlight_differences(self, text):
        self.highlighted_text = ""
        lines = text.split('\n')
        for i in range(len(lines)):
            if len(self.list_of_differences) and i == self.list_of_differences[0]:
                self.highlighted_text += f"\033[91m{lines[i]}\033[0m" + '\n'
                self.list_of_differences.pop(0)
            else:
                self.highlighted_text += lines[i] + '\n'
    

    def get_pdf_differences(self, pdf_correct, pdf_user):

        self.differences = "" 

        text_correct = self.extract_text_from_pdf(pdf_correct)
        text_user = self.extract_text_from_pdf(pdf_user)

        self.compare_texts(text_correct, text_user)