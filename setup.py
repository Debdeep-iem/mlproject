from setuptools import find_packages,setup
from typing import List

def get_requirements(file_path:str)->List[str]:
    requirements=[]
    fp=open(file_path)
    for data in fp:
        if "-e ." in data:
            continue
        requirements.append(data)
    fp.close()
    return requirements


setup(

    name='mlproject',
    version='0.0.1',
    author='Debdeep',
    author_email='debdeeeep@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')
)