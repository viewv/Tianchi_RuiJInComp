from __future__ import print_function
from setuptools import setup, find_packages
import sys

setup(
    name="ssql",
    version="0.1.0",
    author="viewv",
    author_email="zxn@zxnnet.top",
    description="A python Libraries to simplyify sqlite commend",
    long_description=open("README.rst").read(),
    license="MIT",
    url="https://github.com/viewv",
    packages=['ssql'],
    classifiers=[
        "Environment :: Web Environment",
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: Chinese',
        'Operating System :: MacOS',
        'Operating System :: Microsoft',
        'Operating System :: POSIX',
        'Operating System :: Unix',
        'Topic :: Delopemrnt :: SQL',
        "Topic :: SQL",
        "Topic :: Software Development :: Libraries :: Python Modules",
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],
    zip_safe=True,
)
