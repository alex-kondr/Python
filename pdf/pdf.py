from datetime import datetime
from secrets import choice
from fpdf import FPDF
from os import remove
from PyPDF2 import PdfFileReader, PdfFileWriter


entry_number = "entry_number.pdf"
input_file = "1.pdf"
stamp = ["D:/Кондратюк/Личные/Печатка/КЕП+Вх знизу.pdf",
         "D:/Кондратюк/Личные/Печатка/КЕП зверху+Вх знизу.pdf",
         "D:/Кондратюк/Личные/Печатка/КЕП+ЕП знизу.pdf",
         "D:/Кондратюк/Личные/Печатка/КЕП зверху+ЕП знизу.pdf"]


def main():

    number = input("Введіть вхідний номер: ")
    print("Виберіть варіант штампу")

    for i in stamp:
        print(f"i: {stamp[i]}")

    choice_stamp = int(input("Варіант: "))
    date = datetime.today().strftime('"%d".%m.%Y')

    entry_number_date = f'{number}/{date[:-3:-1]}-Вх                {date} р.'

    txt_to_pdf(entry_number_date)
    merge_pdf(input_file, stamp[choice_stamp], entry_number)
    remove("entry_number.pdf")

def merge_pdf(pdf1, pdf2, pdf3):

    with open(pdf1, "rb") as input1:
        input1 = PdfFileReader(input1)

        with open(pdf2, "rb") as input2:
            input2 = PdfFileReader(input2)

            with open(pdf3, "rb") as input3:
                input3 = PdfFileReader(input3)

                input1 = input1.getPage(0)
                input2 = input2.getPage(0)
                input3 = input3.getPage(0)
                input1.mergePage(input2)
                input1.mergePage(input3)

                output = PdfFileWriter()
                output.addPage(input1)
                output.write("output.pdf")

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
