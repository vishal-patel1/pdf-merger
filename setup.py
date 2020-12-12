from setuptools import setup

setup(name="pdfMerger",
      version="1.2",
      description="A pdf merger",
      long_description="An app that merges pdfs into one",
      author="Vishal Patel",
      packages=['code'],
      install_requires=['subprocess', 'importDependency', 'tkinter', 'PyPDF3', 'os'])
