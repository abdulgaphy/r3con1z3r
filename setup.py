import os
import sys
import setuptools
from setuptools.command.install import install

CURRENT_DIR = os.getcwd()
REQUIREMENTS = 'requirements.txt'
requires = [line.strip('\n') for line in open(REQUIREMENTS).readlines()]
with open("README.md", "r") as fh:
    long_description = fh.read()

VERSION = "1.0.3"

setuptools.setup(
    name="R3con1z3r",
    version=VERSION,
    author='Raji Abdulgafar',
    author_email="topeabdulgafar@gmail.com",
    description="R3con1z3r is a lightweight Web information gathering tool with an intuitive features written in python. it provides a powerful environment in which open source intelligence (OSINT) web-based footprinting can be conducted quickly and thoroughly.",
    url="https://github.com/abdulgaphy/r3con1z3r",
    packages=setuptools.find_packages(),
    install_requires=requires,
    long_description=long_description,
    long_description_content_type="text/markdown",
    license="MIT",
    keywords='OSINT web reconnaisance traceroute footprinting DNS',
    classifiers=(
        "Programming Language :: Python",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ),
    # move script depending on platform
    scripts = ['r3con1z3r/scripts/r3con1z3r.bat' if sys.platform.startswith('win') \
                else 'r3con1z3r/scripts/r3con1z3r',
        ],
    package_data={
        '': ['*.*'],
    },
    include_package_data=True,
    zip_safe=False,
)
