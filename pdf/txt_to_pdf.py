from fpdf import FPDF

pdf = FPDF()

pdf.add_page()

pdf.add_font(
    "Times New Roman", "", "font/Times New Roman/times new roman bold.ttf", uni=True)
pdf.set_font("Times New Roman", size=8)

# pdf.cell(180, 0, txt="123/22", ln=1, align="R")
pdf.cell(180, 242, ln=1) #, txt="", ln=1, align="R")
pdf.cell(152, 0, txt="125/22", ln=1, align="R")

pdf.output("pdf_test.pdf")