from setuptools import setup, find_packages
from os import path

here = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='PrintWithPager',
    version='1.0.0',
    description='Simple pager package to help'\
      'with printing output using a pager',
    license='MIT',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/NAndLib/pager',
    author='Andrew Tran',
    author_email='andremail03@gmail.com',
    keywords='pager printer less python',
    packages=find_packages(),
    python_requires='>3'
)
