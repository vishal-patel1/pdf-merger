# global variables
fileName = ""
pdfs = []
outputDirectory = ""

# imports
try:
    import importDependency
    from ttkthemes import ThemedTk 
    from tkinter import ttk, filedialog
    import tkinter as tk
    from PyPDF3 import PdfFileReader, PdfFileMerger
    import os
except ImportError:
    import importDependency
    from ttkthemes import ThemedTk 
    from tkinter import ttk, filedialog
    import tkinter as tk
    from PyPDF3 import PdfFileReader, PdfFileMerger
    import os
"""
logging.basicConfig(
    filename='pdfMerger.log',
    level=logging.DEBUG,
    format='%(asctime)s.%(msecs)03d %(levelname)s %(module)s - %(funcName)s: %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S',
    filemode='a')
    """
#logging.info("graphical app has been launched")

root = ThemedTk(theme="plastik")

root.geometry('475x400')
root.title("Merge PDFs")
#root.tk.call('wm', 'iconphoto', root._w, tk.PhotoImage(file="images/icon.png")
root.iconbitmap("images/icon.icns")
#root.iconphoto(False, tk.PhotoImage(file="images/icon.png"))


def open_files():
    global pdfs

    pdfs = filedialog.askopenfilenames(
        parent=root,
        initialdir='/',
        filetypes=[
            ("pdf", "*.pdf")])
    if pdfs == "":
        output = "please select pdfs to merge"
        #logging.info(output)
        textBox.config(text=output, fg="red")
    else:
        output = "pdfs will be merged"
        #logging.info("pdfs will be merged")
        textBox.config(text=output, fg="black")


def save_as():
    global outputDirectory, fileName

    save = filedialog.asksaveasfilename(
        parent=root,
        initialdir='/')
    if save == "":
        output = "please pick a location and filename"
        #logging.info(output)
        textBox.config(text=output, fg="red")
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
        #logging.info(output)
        textBox.config(text=output, fg="black")


def convert():
    global outputDirectory

    if outputDirectory == "":
        output = "please select where to save the file and a name"
        #logging.info(output)
        textBox.config(text=output, fg="red")
    elif pdfs == "":
        output = "please select pdfs to merge"
        #logging.info(output)
        textBox.config(text=output, fg="red")
    else:
        os.chdir(outputDirectory)
        output = PdfFileMerger()

        for pdf in pdfs:
            input_pdf = PdfFileReader(pdf)
            output.append(input_pdf)

        textBox.config(text="writing the combined pdf")
        #logging.info("writing the combined pdf")
        output.write(fileName)
        textBox.config(text="finished", fg="green")
        #logging.info("finished")


def close():
    root.destroy()
    #logging.info("graphical app has been closed")


fileOpener = ttk.Button(root, text="Open PDFs", command=open_files)
fileOpener.place(x=20, y=20)

saveAsButton = ttk.Button(root, text="Save as", command=save_as)
saveAsButton.place(x=175, y=20)

convertButton = ttk.Button(root, text="Merge!", command=convert)
convertButton.place(x=330, y=20)

textBox = tk.Label(root, font='bold', wraplength=150, justify="center")
textBox.place(x=135, y=100)

ttk.Button(root, text="Quit", command=close).place(x=340, y=360)

root.mainloop()
