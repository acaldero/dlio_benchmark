from setuptools.config import read_configuration
from setuptools import setup


conf_dict = read_configuration("./setup.cfg")
setup(**conf_dict['metadata'])

import os

# for Ubuntu:
# os.system("aptitude install python3-testresources")

  os.system("pip install -r ./requirements.txt")
