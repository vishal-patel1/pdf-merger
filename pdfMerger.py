from PyPDF3 import PdfFileReader, PdfFileMerger
import os

# user defined variables
directory = ""
pdfs = ["",""]
output_name = ".pdf"

os.chdir(directory)

output = PdfFileMerger()

for pdf in pdfs:
    input_pdf = PdfFileReader(pdf)
    output.append(input_pdf)

output.write(output_name)