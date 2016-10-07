from setuptools import setup, find_packages

setup(
    name = "neuropsydia",
    version = "0.0.1",
    packages = find_packages(),
    install_requires = [],
    author = "Dominique Makowski",
    author_email = "dom.makowski@gmail.com",
    maintainer = "Dominique Makowski",
    maintainer_email = "dom.makowski@gmail.com",
    description = ("A Python module for creating experiments, tasks and questionnaires."),
    long_description = open('README.md').read(),
    license = "Mozilla Public License Version 2.0",
    keywords = "python neuropsychology neuropsydia experiment creation",
    url = "https://github.com/neuropsychology/neuropsydia/",
    classifiers = []
    )