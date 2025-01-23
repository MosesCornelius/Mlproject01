from setuptools import List
from setuptools import find_packages,setup


non_required = "- e ."
 
def get_requirements(file_path:str)->List[str]:
    
    """
    this function will return the list of requirements
    """
    
   
    requirements=[]
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        [req.replace("\n","")for req in requirements]
        
        if non_required in requirements:
             return requirements
             
    setup(
    name='MlProject 01', 
    version='0.0.1',
    author='Moses',
    author_email='mosescorneliuscr7@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements("requirements.txt")
)