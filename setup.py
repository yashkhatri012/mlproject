from setuptools import find_packages,setup
from typing import List
def get_requirements(file_path:str)-> List[str]: 
##this func will retun the lists of requiremennts
    requirements=[]

    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        [req.replace('\n', "") for req in requirements]
    return requirements

setup(
    name='mlproject',
    version='0.0.1',
    author='Yash',
    author_email='yashkhati88540@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')
)
 