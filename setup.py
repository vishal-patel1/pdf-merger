from setuptools import setup
setup(name="pdfMerger",
    version="0.9",
    description="A pdf merger",
    long_description="An app that merges pdfs into one",
    author="Vishal Patel",
    packages=['code'],
    install_requires=['logging', 'subprocess', 'importDependency', 'ttkthemes', 'tkinter', 'PyPDF3', 'os'])