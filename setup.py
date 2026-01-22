from setuptools import find_packages, setup
from typing import List

## Take out all packages from requirements
def get_requirements() -> List[str]:
    """
    This function will return the list of packages required for 
    projects from the requirements file
    """
    try:
        with open('requirements.txt','r') as file:
            requirements_lst:List[str]=[]
            lines=file.readlines()
            for line in lines:
                requirement=line.strip()
                ## ignore empty lines and -e .
                if requirement and requirement!='-e .':
                    requirements_lst.append(requirement)
    except FileNotFoundError:
        print("requiremets.txt file not found")

    return requirements_lst

setup(
   name='NetworkSecurity',
   version='1.0',
   description='This is a network-security project',
   author='Shivam Singh',
   author_email='shivamsingh22188@gmail.com',
   packages=find_packages(),
   install_requires=get_requirements(), #external packages as dependencies
)

if __name__ == "__main__":
    packages_lst=get_requirements()
    print(f"Printing packages: {packages_lst}")
    print(f"packages Types: {type(packages_lst)}")

