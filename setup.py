from setuptools import setup
setup(name="pdfMerger",
    version="1.0",
    description="A pdf merger",
    long_description="An app that merges pdfs into one",
    author="Vishal Patel",
    packages=['code'],
    install_requires=['subprocess', 'importDependency', 'ttkthemes', 'tkinter', 'PyPDF3', 'os'])