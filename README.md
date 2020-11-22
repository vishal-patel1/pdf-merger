# Running the Program

## Dependencies

* Python 3 + libraries below
  * [PyPDF3][1]
  * os

## Usage

1. Define the following variables in pdfMerger.py
    * directory as a __string__
    * pdfs as a __list__ filled with __strings__
    * output_name as a __string__
  
```python
# user defined variables
directory = ""
pdfs = ["",""]
output_name = ".pdf"
```

2. Run the program
```console
user@lt:~$ python3 pdfMerger.py
```

[1]: https://pypi.org/project/PyPDF3/