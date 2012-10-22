import os
from setuptools import setup

# Utility function to read the README file.
# Used for the long_description.  It's nice, because now 1) we have a top level
# README file and 2) it's easier to type in the README file than to put a raw
# string in below ...
# http://packages.python.org/an_example_pypi_project/setuptools.html#setting-up-setup-py
def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name = "mxit_ga",
    version = "0.1.0",
    author = "Konrad Blum",
    author_email = "konrad@kblum.com",
    description = "Python module to perform Google Analytics tracking for Mxit web applications.",
    license = "MIT",
    keywords = "google analytics mxit",
    url = "https://github.com/kblum/mxit-ga-py",
    download_url = "https://github.com/kblum/mxit-ga-py/downloads",
    packages = ["mxit_ga",],
    long_description = read("README.md"),
    classifiers = [
        "Development Status :: 4 - Beta",
        "Programming Language :: Python",
        "Intended Audience :: Developers",
        "Operating System :: OS Independent",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "License :: OSI Approved :: MIT License",
    ]
)
