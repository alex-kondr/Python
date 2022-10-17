import PyPDF2

input_file = "1.pdf"
output_file = "11.pdf"
mark_file = "mark_txt.pdf"

with open(input_file, "rb") as file_input:

    pdf = PyPDF2.PdfFileReader(file_input)

    with open(mark_file, "rb") as file_mark:
        mark = PyPDF2.PdfFileReader(file_mark)

        first_page = pdf.getPage(0)
        first_page_mark = mark.getPage(0)

        first_page.mergePage(first_page_mark)

        pdf_writer = PyPDF2.PdfFileWriter()
        pdf_writer.addPage(first_page)

        with open(output_file, "wb") as file_output:
            pdf_writer.write(file_output)
