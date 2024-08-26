# -*- coding: utf-8 -*-
"""
Created on Mon Aug 26 14:09:37 2024

@author: acer
"""

from setuptools import find_packages, setup
from typing import List

def parse_requirements(file_path: str) -> List[str]:
    """
    This function reads the requirements file and returns a list of dependencies.
    """
    dependencies = []
    with open(file_path, 'r') as file:
        dependencies = file.read().splitlines()

        if '-e .' in dependencies:
            dependencies.remove('-e .')

    return dependencies

setup(
    name='GPVS-Fault-Detection',
    version='0.0.1',
    author='Anila',
    author_email='anilamathew414@gmail.com',
    packages=find_packages(),
    install_requires=parse_requirements('requirements.txt')
)
