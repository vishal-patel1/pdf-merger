# imports
import subprocess, sys

# variables
dependencies = ['PyPDF3', 'setuptools', 'git+https://github.com/RedFantom/ttkthemes']

# function to install apps 
def install(app):
    subprocess.call('pip3 install ' + app, shell=True)

# install the apps
for dependency in dependencies:
    install(dependency)