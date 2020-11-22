from PyPDF3 import PdfFileReader, PdfFileWriter, PdfFileMerger
import os

# user defined variables
directory = "/Users/vishal/Desktop"
pdfs = ["FromNature_Emerson.pdf","CivilDisobedience_Thoreau.pdf"]
output_name = "combined.pdf"

os.chdir(directory)

output = PdfFileMerger()

for pdf in pdfs:
    input_pdf = PdfFileReader(pdf)
    output.append(input_pdf)

output.write(output_name) 