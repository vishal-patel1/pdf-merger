# global variables
fileName = ""
pdfs = []
outputDirectory = ""
osType = ""

# imports
try:
    import importDependency
    from tkinter import filedialog
    import tkinter as tk
    from PyPDF3 import PdfFileReader, PdfFileMerger
    import os
except ImportError:
    import importDependency
    from tkinter import filedialog
    import tkinter as tk
    from PyPDF3 import PdfFileReader, PdfFileMerger
    import os

root = tk.Tk()
TK_SILENCE_DEPRECATION = 1

root.geometry('475x400')
root.title("Merge PDFs")


def open_files():
    global pdfs

    pdfs = filedialog.askopenfilenames(
        parent=root,
        initialdir='/',
        filetypes=[
            ("pdf", "*.pdf")])
    if pdfs == "":
        output = "please select pdfs to merge"
        textBox.config(text=output, fg="red", justify="center")
    else:
        output = "pdfs will be merged"
        textBox.config(text=output, fg="black", justify="center")


def save_as():
    global outputDirectory, fileName

    save = filedialog.asksaveasfilename(
        parent=root,
        initialdir='/')
    if save == "":
        output = "please pick a location and filename"
        textBox.config(text=output, fg="red", justify="center")
    else:
        index = save.rfind('/')

        outputDirectory = save[0:index]
        fileName = save[index + 1:len(save)]
        if ".pdf" in fileName:
            fileName = fileName
        elif ".pdf" not in fileName:
            fileName += ".pdf"
        else:
            fileName = "merge.pdf"
        output = "file will be saved at " + outputDirectory + " as " + fileName
        textBox.config(text=output, fg="black", justify="center")


def convert():
    global outputDirectory

    if outputDirectory == "":
        output = "please select where to save the file and a name"
        textBox.config(text=output, fg="red", justify="center")
    elif pdfs == "":
        output = "please select pdfs to merge"
        textBox.config(text=output, fg="red", justify="center")
    else:
        os.chdir(outputDirectory)
        output = PdfFileMerger()

        for pdf in pdfs:
            input_pdf = PdfFileReader(pdf)
            output.append(input_pdf)

        textBox.config(text="writing the combined pdf", justify="center")
        output.write(fileName)
        textBox.config(text="finished", fg="green", justify="center")


def close():
    root.destroy()


fileOpener = tk.Button(root, text="Open PDFs", command=open_files)
fileOpener.place(x=20, y=20)

saveAsButton = tk.Button(root, text="Save as", command=save_as)
saveAsButton.place(x=175, y=20)

notice = tk.Label(root, text="Notices: \n "
                             "1) To ensure that the pdfs are merged in the proper order, "
                             "please name the pdfs in alphabetical order.  "
                             "\n 2) Before merging pdfs directly from a scanner,"
                             " open them up with a PDF editor and immediately "
                             "save the document.", wraplength=250, justify="center")
notice.place(x=105, y=230)

convertButton = tk.Button(root, text="Merge!", command=convert)
convertButton.place(x=330, y=20)

textBox = tk.Label(root, font='bold', wraplength=150, justify="center")
textBox.place(x=135, y=100)

tk.Button(root, text="Quit", command=close).place(x=370, y=360)

root.mainloop()
