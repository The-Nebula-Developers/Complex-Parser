from setuptools import find_packages, setup

with open("complex_parser\\README.md", "r") as f:
    long_description = f.read()

setup(
    name="complex_parser",
    version="0.0.1.2",
    description="A versatile Python package for data extraction from JSON-like structures with user-defined format keys, enhanced with synonym retrieval capabilities.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/The-Nebula-Developers/Complex-Parser",
    author="The Nebula Developer",
    author_email="support@nebuladevs.tech",
    license="Mozilla Public License Version 2.0",
    keywords=["python","data","parsing","json","complex","synonyms","similar","custom parsing","data parser","synomym data parser","keyword extractor","fuzzywuzzy","nltk","words","json data"],
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
    packages=find_packages(),
    python_requires=">=3.10",
    install_requires=[
        "fuzzywuzzy>=0.18.0",
        "nltk>=3.6.2",
    ],
    extras_require={
        "dev": ["twine"]
    }
)