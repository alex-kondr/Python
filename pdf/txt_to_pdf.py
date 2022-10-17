from fpdf import FPDF

pdf = FPDF()

pdf.add_page()

pdf.add_font("DejaVu", "", "font/DejaVuSansMono.ttf", uni=True)
pdf.set_font("DejaVu", size=8)

# pdf.cell(180, 0, txt="123/22", ln=1, align="R")
pdf.cell(180, 242, ln=1) #, txt="", ln=1, align="R")
pdf.cell(152, 0, txt="125/22", ln=1, align="R")

pdf.output("pdf_test.pdf")