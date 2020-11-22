try:
    import os
    import tkinter as tk
    import tkinter.ttk as ttk
    from tkinter import filedialog
    from PyPDF3 import PdfFileReader, PdfFileMerger
except ImportError:
    import tkinter as tk
    import tkinter.ttk as ttk
    from tkinter import filedialog
 
root = tk.Tk()
root.geometry('600x400')
root.title("Merge PDFs")

style = ttk.Style(root)
style.theme_use("clam")

#global variables
fileName = ""
pdfs = []
outputDirectory = ""

def openFiles():
    global pdfs
    pdfs = filedialog.askopenfilenames(
    	parent=root,
    	initialdir='/',
    	filetypes=[
    		("pdf", "*.pdf")])

def getFileName():
    global fileName
    global e

    fileName = e.get()

    if(".pdf" in fileName):
        fileName = fileName
    elif(".pdf" not in fileName):
        fileName += ".pdf"
    else:
        fileName = "merge.pdf"

    output = "file will be saved as " + fileName
    textBox.config(text=output)

def openOutputDirectory():
    global outputDirectory, textBox
    outputDirectory = filedialog.askdirectory(
        parent = root,
        initialdir='/'
    )

    output = "file will be saved at " + outputDirectory
    textBox.config(text=output)

def convert():
    global outputDirectory
    os.chdir(outputDirectory)
    output = PdfFileMerger()

    for pdf in pdfs:
        input_pdf = PdfFileReader(pdf)
        output.append(input_pdf)

    textBox.config(text="writing the combined pdf")
    output.write(fileName)
    textBox.config(text="finished")

fileOpener = ttk.Button(root, text="Open PDFs", command=openFiles)
fileOpener.grid(row=1, column=0, padx=4, pady=4, sticky='ew')

e = ttk.Entry(root)
e.grid(row=1, column=1, padx=4, pady=4, sticky='ew')

confirmFileName = ttk.Button(root, text="Confirm File Name", command=getFileName)
confirmFileName.grid(row=2, column=1, padx=4, pady=4, sticky='ew')

fileSaver = ttk.Button(root, text="Save File At", command = openOutputDirectory)
fileSaver.grid(row=1, column=2)

convertButton = ttk.Button(root, text="Merge!", command=convert)
convertButton.grid(row=1, column=3, padx=4, pady=4, sticky='ew')

textBox = tk.Label(root, fg="red")
textBox.grid(row = 5, column=1, padx=4, pady=4, sticky='ew')

root.mainloop()