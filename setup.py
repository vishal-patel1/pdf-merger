from setuptools import setup
setup(name="pdfMerger",
    version="1.1",
    description="A pdf merger",
    long_description="An app that merges pdfs into one",
    author="Vishal Patel",
    packages=['code'],
    install_requires=['PyPDF3'],
    setup_requires=["py2app"])