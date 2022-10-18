from datetime import datetime
from fpdf import FPDF
from os import remove
from PyPDF2 import PdfFileReader, PdfFileWriter


input_file = "1.pdf"
# output_file = "output.pdf"
stamp = "stamp.pdf"
entry_number = "entry_number.pdf"

def main():

    number = input("Enter the entry number: ")
    date = datetime.today().strftime("%d.%m.%Y")

    entry_number_date = f'{number}/{date[:-3:-1]}-Вх                {date} р.'

    txt_to_pdf(entry_number_date)
    time = merge_pdf(input_file, stamp)
    merge_pdf(f"output{time}.pdf" , entry_number)
    remove("entry_number.pdf")
    remove(f"output{time}.pdf")


def merge_pdf(pdf1, pdf2):

    with open(pdf1, "rb") as input1:
        input1 = PdfFileReader(input1)

        with open(pdf2, "rb") as input2:
            input2 = PdfFileReader(input2)

            input1 = input1.getPage(0)
            input2 = input2.getPage(0)
            input1.mergePage(input2)

            output = PdfFileWriter()
            output.addPage(input1)
            time = datetime.now().strftime("%H.%M.%S")
            output.write(f"output{time}.pdf")
            
    return time

def txt_to_pdf(txt):
    pdf = FPDF()
    pdf.add_page()

    pdf.add_font("Times New Roman", "", 
                 "font/Times New Roman/times new roman bold.ttf", uni=True)

    pdf.set_font("Times New Roman", size=9)
    pdf.cell(180, 241, ln=1)
    pdf.cell(188, 0, txt=txt, ln=1, align="R")

    pdf.output("entry_number.pdf")

if __name__ == "__main__":
    main()
