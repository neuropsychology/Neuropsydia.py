from setuptools import setup, find_packages
import re

# ------------------
def find_version():
    result = re.search(r'{}\s*=\s*[\'"]([^\'"]*)[\'"]'.format("__version__"), open('neurokit/__init__.py').read())
    return result.group(1)
# ------------------

setup(
name = "neuropsydia",
description = ("A Python Module for Creating Experiments, Tasks and Questionnaires."),
version = find_version(),
license = "Mozilla Public License Version 2.0",
author = "Dominique Makowski",
author_email = "dom.makowski@gmail.com",
maintainer = "Dominique Makowski",
maintainer_email = "dom.makowski@gmail.com",
packages = find_packages(),
package_data = {
	"neuropsydia.files.font":["*.ttf"],
	"neuropsydia.files.binary":["*.png"],
	"neuropsydia.files.logo":["*.png"]},
install_requires = [
    'pygame',
    'numpy',
    'pandas',
    'Pillow',
    'neurokit',
    'pyxid',
    'python-docx',
    'cryptography',
    'statsmodels'],
dependency_links=[
	"https://github.com/neuropsychology/NeuroKit.py/zipball/master"],
long_description = open('README.rst').read(),
keywords = "python neuropsychology neuropsydia experiment creation",
url = "https://github.com/neuropsychology/Neuropsydia.py/",
download_url = 'https://github.com/neuropsychology/Neuropsydia.py/zipball/dev',
test_suite='nose.collector',
tests_require=['nose'],
classifiers = [
	'Intended Audience :: Science/Research',
	'Intended Audience :: Developers',
	'Programming Language :: Python',
	'Topic :: Software Development',
	'Topic :: Scientific/Engineering',
	'Operating System :: Microsoft :: Windows',
	'Operating System :: Unix',
	'Operating System :: MacOS',
	'Programming Language :: Python :: 3.5',
	'Programming Language :: Python :: 3.6']
)
