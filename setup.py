from setuptools import find_packages, setup
from typing import List

HYPEN_E_DOT = '-e .'

def get_requirements(file_path:str)->List[str]:
    requirements = []
    with open(file_path) as f:
        requirements = f.readlines()
        requirements = [req.replace('\n','') for req in requirements]
    
        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)
    
    return requirements



setup(

name='End to End Project',
version='0.1.0',
description='A project for Book Recommendation System',
long_description=open('README.md').read(),
url='',
author='Abdullah Ateeq',
author_email='abdullahateeq852@gmail.com',
license='MIT',
packages=find_packages(),
install_requires= get_requirements('requirements.txt')



)