# setup.py
from setuptools import setup, find_packages

setup(
    name='simport',
    version='1.0.0',
    description='A Python package to import modules dynamically using relative paths',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    author='Andrew Belonogov',
    author_email='andrew_belonogov@techaccountingpro.com',
    url='https://github.com/andrewfowl/simport',  # Link to the GitHub repository
    packages=find_packages(),
    include_package_data=True,
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
)
