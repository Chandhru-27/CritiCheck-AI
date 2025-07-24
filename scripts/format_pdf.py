from fpdf import FPDF
import textwrap
import re

class FeedbackPDF(FPDF):
    def __init__(self):
        super().__init__()
        self.add_page()
        self.add_font("DejaVu", "", "DejaVuSans.ttf", uni=True) # replace .ttf with font file path
        self.set_font("DejaVu", "", 12)

    def wrap_line(self, line, width=80):
        return '\n'.join(textwrap.wrap(line, width=width))

    def clean_text(self, text):
        return re.sub(r'[^\x20-\x7E]', '', text)  

    def add_feedback(self, text):
        cleaned = self.clean_text(text)
        for line in cleaned.split('\n'):
            wrapped = self.wrap_line(line)
            self.multi_cell(0, 10, wrapped)
    
        

