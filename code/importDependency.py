# imports
import subprocess

# variables
dependencies = {
    'PyPDF3': 'PyPDF3',
    'setuptools': 'setuptools'
}

# install the apps
for key, value in dependencies.items():
    try:
        __import__(key)
    except ModuleNotFoundError:
        subprocess.call('pip3 install ' + value, shell=True)
