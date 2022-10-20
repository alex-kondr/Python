from datetime import datetime
from fpdf import FPDF
from os import remove
from pathlib import Path
from PyPDF2 import PdfFileReader, PdfFileWriter, PdfMerger
import pikepdf



TEMP_FOLDER = Path("D:/Кондратюк/Личные/Штамп/Для штампів")
TEMP_PDF = TEMP_FOLDER.joinpath("temp.pdf")
ENTRY_NUMBER = TEMP_FOLDER.joinpath("entry_number.pdf")
STAMP = {"1": "Без-КЕП+Вх.pdf",
         "2": "КЕП+Вх.pdf",
         "3": "Без-КЕП+ЕП.pdf",
         "4": "КЕП+ЕП.pdf"}


def find_file():
    for file in Path().iterdir():
        if file.is_file() and file.suffix == ".pdf":
            return file

def main():

    input_file = find_file()
    file_name = input_file.name

    if not input_file:
        print("Файл не знайдений")
        input("Натисніть ентер для закриття")
        quit()

    number = input("Введіть вхідний номер: ")
    print("Виберіть варіант штампу")

    for i, value in STAMP.items():
        print(f"{i}: {value}")

    number_stamp = input("Варіант: ")
    
    

    stamp = TEMP_FOLDER.joinpath(STAMP[number_stamp])
    date = datetime.today().strftime('"%d"  %m  %Y')

    if number_stamp == "1" or number_stamp == "2":
        count_space = (" " * 16)[len(number)*2:]
        entry_number_date = f'{number}/{date[:-3:-1]}-Вх{count_space}{date} р.'
    elif number_stamp == "3" or number_stamp == "4":
        count_space = (" " * 8)[len(number)*2:]
        entry_number_date = f'{number}/{date[:-3:-1]}-Вх{count_space}{date} р.'

    print(len(count_space))
    txt_to_pdf(entry_number_date)

    with pikepdf.Pdf.open(input_file) as input_pdf:
        input_pdf.save(TEMP_PDF)

    merge_pdf(TEMP_PDF, stamp, ENTRY_NUMBER, file_name)
    remove(ENTRY_NUMBER)
    remove(TEMP_FOLDER.joinpath("done.pdf"))
    remove(TEMP_PDF)

def merge_pdf(pdf1, pdf2, pdf3, file_name):

    with open(pdf1, "rb") as input1:
        input1 = PdfFileReader(input1)
        numb_pages = input1.getNumPages()

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
                output.write(TEMP_FOLDER.joinpath("done.pdf"))

                merger = PdfMerger()
                merger.append(TEMP_FOLDER.joinpath("done.pdf"))
                merger.append(pdf1, pages=(1, numb_pages))
                merger.write("done_" + file_name)
                merger.close()


def txt_to_pdf(txt):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_auto_page_break(auto=True, margin=0.0)

    pdf.add_font("Times New Roman", "", 
                 TEMP_FOLDER.joinpath("font/Times New Roman/times new roman.ttf"), uni=True)

    pdf.set_font("Times New Roman", size=10)
    pdf.cell(0, 276, ln=2)
    pdf.cell(198, 0, txt=txt, ln=2, align="R")

    pdf.output(ENTRY_NUMBER)

if __name__ == "__main__":
    main()
