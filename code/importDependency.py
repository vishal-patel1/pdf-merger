# imports
import subprocess

# variables
dependencies = {
    'PyPDF3': 'PyPDF3',
    'setuptools': 'setuptools',
    'ttkthemes': 'git+https://github.com/RedFantom/ttkthemes'
}

# install the apps
for key,value in dependencies.items():
    try:
        __import__(key)
    except:
        subprocess.call('pip3 install ' + value, shell=True)
