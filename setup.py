from setuptools import find_packages, setup
from typing import List

Hypen_dot = "-e ."
def get_requirements(file_path:str)->List[str]:
    """
    this function will return the list of requirements
    """
    req = []
    with open(file_path) as file_obj:
        req = file_obj.readlines()
        req = [r.replace("\n", "") for r in req]

        if Hypen_dot in req:
            req.remove(Hypen_dot)
    return req

setup(
name="mlProject",
version="0.0.1",
author="Kapil",
author_email="kapilbbansal@gmail.com",
packages= find_packages(),
#install_requires=['numpy', 'pandas', 'matplotlib', 'sklearn']
install_requires=get_requirements("requirements.txt") 
)