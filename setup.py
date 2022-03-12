from setuptools import setup, find_packages
import os

here = os.path.abspath(os.path.dirname(__file__))

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = "\n" + fh.read()

VERSION = "0.2.3"
DESCRIPTION = "UNOFFICIAL Python bindings for Honeygain Dashboard API"
LONG_DESCRIPTION = "A package that allows you to connect to Honeygain (HG) API and interact with your data."

# Setting up
setup(
    name = "pyHoneygain",
    version = VERSION,
    author = "coder-amogh (Amogh Datar)",
    description = DESCRIPTION,
    long_description_content_type = "text/markdown",
    long_description = long_description,
    packages = find_packages(),
    install_requires = ['requests', 'pySocks'],
    url = "https://github.com/coder-amogh/pyHoneygain",
    project_urls = {
        "Bug Tracker": "https://github.com/coder-amogh/pyHoneygain/issues",
    },
    keywords = ['python', 'honeygain', 'hg', 'passive income', 'honeygain api', 'honeygain dashboard', "python honeygain"],
    classifiers = [
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ]
)
