# imports
import subprocess
#import #logging

# variables
dependencies = {
    'PyPDF3': 'PyPDF3',
    'setuptools': 'setuptools',
    'ttkthemes': 'git+https://github.com/RedFantom/ttkthemes'
}

"""logging.basicConfig(
    filename='pdfMerger.log',
    level=#logging.DEBUG,
    format='%(asctime)s.%(msecs)03d %(levelname)s %(module)s - %(funcName)s: %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S',
    filemode='a'
)"""
#logging.info("ImportDependency.py has been opened")

# install the apps
for key,value in dependencies.items():
    try:
        __import__(key)
        #logging.info(key + " has been imported")
    except:
        subprocess.call('pip3 install ' + value, shell=True)
        #logging.info(value + " has been installed")

#logging.info("ImportDependency.py has been closed")
