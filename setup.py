from setuptools import find_packages, setup
from typing import List

def get_requirements(file_path:str)->List[str]:
    '''this function will return the list of requirements
    '''
    reqirements=[]

    with open(file_path) as file_obj:
        requirements=file_obj.readline()
        [req.replace('\n',"") for req in requirements]

    return requirements








setup(
    name='mlproject',
    version='0.0.1',
    author='bhartendu',
    author_email='bhartenduanand1@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')
)