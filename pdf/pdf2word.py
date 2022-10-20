from pathlib import Path
from pdf2docx import parse
from PyPDF2 import PdfFileReader, PdfFileWriter, PdfMerger

# file = Path("11.pdf").resolve()


# def find_file():
#     for file in Path().iterdir():
#         if file.is_file() and file.suffix == ".pdf":
#             return file


# file = find_file()
# start = int(input("Введіть початковий номер сторінки:")) - 1
# end = int(input("Введіть кінцеву сторінку: "))


# merger = PdfMerger()
# merger.append(file, pages=(start, end))
# merger.write("done_" + file.name)
# merger.close()

# parse(str("done_" + file.name), f"{file.parent.resolve()}/{file.name}.docx")
parse("1.pdf", "1.docx")
