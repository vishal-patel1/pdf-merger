try:
    import os
    import tkinter as tk
    import tkinter.ttk as ttk
    from tkinter import filedialog
    from PyPDF3 import PdfFileReader, PdfFileMerger
except ImportError:
    import Tkinter as tk
    import ttk
    import tkFileDialog as filedialog
 
root = tk.Tk()
root.geometry('400x400')

style = ttk.Style(root)
style.theme_use("clam")
 
def openFilesAndConvert():
    pdfs = filedialog.askopenfilenames(
    	parent=root,
    	initialdir='/',
    	filetypes=[
    		("pdf", "*.pdf")])

    output = PdfFileMerger()
    for pdf in pdfs:
        input_pdf = PdfFileReader(pdf)
        output.append(input_pdf)

    print("writing the combined pdf")
    output.write("idkifthiswillwork.pdf")
    print("finished")


ttk.Button(root, text="Open files", command=openFilesAndConvert).grid(row=1, column=0, padx=4, pady=4, sticky='ew')
e = ttk.Entry(root, width=50)
e.pack()

name = tk.StringVar()


root.mainloop()
