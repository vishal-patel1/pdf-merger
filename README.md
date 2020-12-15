# Running the Program

## Dependencies

* Python 3 + libraries below
  * [PyPDF3][1]
  * tkinter 8.6 or above
  * setuptools
  * os
  * subprocess

## Building

1. Download this repository
```console
user@lt:~$ gh repo clone vishal-patel1/pdf-merger
```

or 

```console
user@lt:~$ git clone https://github.com/vishal-patel1/pdf-merger
```

or 

![img.png](img.png)

2. Run the program [graphical.py][3] with python3 to launch the GUI application


```console
user@lt:~$ python3 pdf-merger/code/graphical.py
```
Now skip to and follow the Execution instructions

### Automatically
1. Download a packaged application from these [releases][5] if a release supports your operating system

2. Launch the [graphical.py][3] using python3

Now skip to and follow the Execution instructions

## Execution

1. Now that you launched the program, open some pdfs using the "Open PDFs" button

![img_1.png](img_1.png)
   
2. Click "Save as" to locate a directory that you want the merged PDF to be and be sure to give it a name!

![img_2.png](img_2.png)
   
3. Click "Merge!" to begin building the new, combined PDF

![img_3.png](img_3.png)

```console
user@lt:~$ ls
Output.pdf
```

## Licensing

Find more details about the licensing [here][4]

[1]: https://github.com/sfneal/PyPDF3
[2]: code/importDependency.py
[3]: code/graphical.py
[4]: LICENSE.md
[5]: https://github.com/vishal-patel1/pdf-merger/releases