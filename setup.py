from setuptools import setup, find_packages

# To use a consistent encoding
from codecs import open
from os import path

# The directory containing this file
HERE = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with open(path.join(HERE, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

# This call to setup() does all the work
setup(
    name="polygon-api-access-nn2094",
    version="0.2.0",
    description="Library for Homework",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://polygon-api-access-nn2094.readthedocs.io/",
    author="Nilansh Netan",
    author_email="nn2094@nyu.edu",
    license="MIT",
    classifiers=[
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Operating System :: OS Independent"
    ],
    packages=["polygon_access"],
    include_package_data=True,
    install_requires=["polygon-api-client", "SQLAlchemy"]
)