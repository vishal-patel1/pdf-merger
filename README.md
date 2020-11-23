# Running the Program

## Dependencies

* Python 3 + libraries below
  * [PyPDF3][1]
  * os
  * lots of tkinter stuff
  * [ttkthemes][3]

## Usage

1. Define the following variables in [pdfMerger.py][2]
    * directory as a __string__
    * pdfs as a __list__ filled with __strings__
    * output_name as a __string__
  
```python
# user defined variables
directory = "~/Desktop"
pdfs = ["1.pdf","2.pdf"]
output_name = "merged.pdf"
```

2. Run the program

```console
user@lt:~$ python3 pdfMerger.py
```

3. Find the merged pdf

```console
user@lt:~$ ls
merged.pdf
```

[1]: https://pypi.org/project/PyPDF3/
[2]: pdfMerger.py
[3]: https://ttkthemes.readthedocs.io/en/latest/installation.html