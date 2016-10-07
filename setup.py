from setuptools import setup, find_packages

setup(
    name = "neuropsydia",
    version = "0.0.1",
    packages = find_packages(),
    install_requires = ['pygame>=1.9.2', 'numpy>=1.11.0', 'pandas>=0.18.0', 'Pillow>=3.0.0', 'plotly>=1.12.9', 'scipy>=0.17.0'],
	# dependency_links = ['https://bitbucket.org/pygame/pygame/get/tip.zip#egg=pygame-1.9.2'],
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
