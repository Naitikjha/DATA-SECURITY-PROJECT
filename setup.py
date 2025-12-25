from setuptools import find_packages,setup
from typing import List

def get_requirments()->list[str]:
    lst_requirments:list[str]=[]
    try:
        with open('requirements.txt','r') as file:
        
            lines=file.readlines()
            for line in lines:
                requirments=line.strip()
                if requirments and requirments!= '-e .':
                    lst_requirments.append(requirments)
    except FileNotFoundError:
        print("requirments.txt file not found")
    return lst_requirments
setup(
   name="network_security",
    version="0.0.1",
    author="Naitik kumar Jha",
    author_email="naitikjha1845@gmail.com",
    packages=find_packages(),
    install_requires=get_requirments()

)