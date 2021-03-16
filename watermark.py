import PyPDF2
import sys


def pdf_combiner(pdf_list):
    merger = PyPDF2.PdfFileMerger()
    for pdf in pdf_list:
        print(pdf)
        merger.append(pdf)
    merger.write('super.pdf')


input_pdf = sys.argv[1]
watermark_pdf = sys.argv[2]

with open(input_pdf, 'rb') as input_file:
    input_reader = PyPDF2.PdfFileReader(input_file)
    with open(watermark_pdf, 'rb') as watermark_file:
        watermark_reader = PyPDF2.PdfFileReader(watermark_file)
        watermark_page = watermark_reader.getPage(0)

        writer = PyPDF2.PdfFileWriter()

        for page in range(input_reader.numPages):
            input_page = input_reader.getPage(page)
            input_page.mergePage(watermark_page)
            writer.addPage(input_page)

        with open('secret.pdf', 'wb') as output_file:
            writer.write(output_file)
