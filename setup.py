# Work in Progress

import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="PDF-Merger",
    version="0.9.1",
    scripts=['graphical.py'],
    author="Vishal Patel",
    author_email="vis142022@gmail.com",
    description="a PDF merger",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/vishal-patel1/pdf-merger/blob/main/README.md",
    packages=setuptools.find_packages(),
    data_files=[(
        'images', ['icon.png', 'icon.ico']
    )],
    py_modules = ['os', 'ttkthemes', 'tkinter', 'PyPDF3'],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",

    ],
    python_requires='>=3.7',
)