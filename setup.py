from setuptools import setup
from typing import List



#Declaring variables for setup function
PROJECT_NAME="pressure-level-predictor"
VERSION="0.0.3"
AUTHOR="Lalita"
DESCRIPTION="This is pressure level predictor ML project"
PACKAGES=["airfoil"]
REQUIREMENT_FILE_NAME="requirements.txt"


def get_requirements_list()->List[str]:
    '''
    Description: This function is going to return list of requirement
    mention in requirements.txt file

    return: This function is going to return a list which contain name of libraries
    mentioned in requirements.txt file
    '''
    with open (REQUIREMENT_FILE_NAME) as requirement_file:
        return requirement_file.readlines().remove("-e .")



setup(
    name=PROJECT_NAME,
    version=VERSION,
    author=AUTHOR,
    description=DESCRIPTION,
    packages=PACKAGES,
    install_requires=get_requirements_list()
    
)

if __name__=='__main__':
    print(get_requirements_list())