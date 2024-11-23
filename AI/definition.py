import pdfplumber


class Definition:

    def __init__(self) -> None:
        self.differences = ""
        self.highlited_text = ""

    def extract_text_from_pdf(self, path):
        text = ''
        with pdfplumber.open(path) as pdf:
            for page in pdf.pages:
                text += page.extract_text() + '\n'
        return text

    def compare_texts(self, text1, text2):

        lines1 = text1.split('\n')
        lines2 = text2.split('\n')

        for line1, line2 in zip(lines1, lines2):
            if line1 != line2:
                self.differences+=f"First sentence: {line1}\nSecond sentence: {line2}\n"
    
    def highlight_differences(self, text, list_of_differences):
        lines = text.split('\n')
        for i in list_of_differences:
            self.highlited_text += f"\033[91m{lines[i]}\033[0m" + '\n'

        highlighted_text = '\n'.join(lines)

        return highlighted_text.encode('utf-8')
    def get_pdf_differences(self, pdf_correct, pdf_user):

        self.differences = "" 

        text_correct = self.extract_text_from_pdf(pdf_correct)
        text_user = self.extract_text_from_pdf(pdf_user)

        self.compare_texts(text_correct, text_user)

