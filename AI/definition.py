import pdfplumber


class Definition:

    def __init__(self) -> None:
        self.differences = [] 

    def extract_text_from_pdf(self, path):
        text = ''
        with pdfplumber.open(path) as pdf:
            for page in pdf.pages:
                text += page.extract_text() + '\n'  # Adding a newline character for better readability
        return text

    def compare_texts(self, text1, text2):

        lines1 = text1.split('\n')
        lines2 = text2.split('\n')
        for line1, line2 in zip(lines1, lines2):
            if line1 != line2:
                self.differences.append([line1, line2])
        

    def get_differences(self, pdf_first, pdf_second):
        pdf_path1 = 'Ziadost_filled.pdf'
        pdf_path2 = 'Ziadost_user.pdf'

        text1 = self.extract_text_from_pdf(pdf_path1)
        text2 = self.extract_text_from_pdf(pdf_path2)

        self.compare_texts(text1, text2)

# definition = Definition()
# pdf_path1 = 'Ziadost_filled.pdf'
# pdf_path2 = 'Ziadost_user.pdf'

# definition.get_differences(pdf_path1, pdf_path2)

# print(definition.differences)