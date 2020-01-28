import PyPDF2
import sys

input_file = sys.argv[1]
output_file = sys.argv[2]

pdf_in = open(input_file, 'rb')
pdf_reader = PyPDF2.PdfFileReader(pdf_in)
pdf_writer = PyPDF2.PdfFileWriter()

for pagenum in range(pdf_reader.numPages):
  page = pdf_reader.getPage(pagenum)
  page.rotateClockwise(270)
  pdf_writer.addPage(page)

pdf_out = open(output_file, 'wb')
pdf_writer.write(pdf_out)
pdf_out.close()
pdf_in.close()
