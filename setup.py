#!/usr/bin/env python

from setuptools import setup

setup(
    name = "MRAA594Shift",
    version = "0.1.0",
    author = "Patric Lintschinger",
    author_email = "lint_patric@cable.vol.at",
    description = ("A module for interfacing a 594 shift register with a board who runs MRAA (intel iot)"),
    license = "MIT",
    keywords = "MRAA pi bbb 594 shift register electronics",
    url = "http://github.com/Respekt1/MRAA594Shift",
    packages=['MRAA594Shift'],
    long_description = (""),
    classifiers = [
        "Development Status :: 1 - Alpha",
        "Environment :: Other Environment",
        "License :: OSI Approved :: MIT",
        "Operating System :: POSIX :: Linux",
        "Programming Language :: Python",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
)
