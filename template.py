import os #os library
from pathlib import Path # for determining the path
import logging # for inbit login

logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s:')

project_name = "textsummerizer"

list_of_files = [
    ".github/workflows/.gitkeep",
    f"src/{project_name}/__init__.py",    
    f"src/{project_name}/components/__init__.py",    
    f"src/{project_name}/utils/__init__.py",
    f"src/{project_name}/utils/common.py",
    f"src/{project_name}/logging/__init__.py",
    f"src/{project_name}/config/__init__.py",
    f"src/{project_name}/config/cofiguration.py",
    f"src/{project_name}/pipline/__init__.py",
    f"src/{project_name}/entity/__init__.py",
    f"src/{project_name}/constants/__init__.py",
    "config/config.yaml",
    "params.yaml",
    "app.py",
    "main.py"
    "Dockerfile",
    "requirements.txt",
    "setup.py",
    "research/trails.ipynb",
    "test.py",
]


for filepath in list_of_files:
    filepath = Path(filepath)
    fildir, filename = os.path.split(filepath)

    if fildir !="":
        os.makedirs(fildir,exist_ok=True)
        logging.info("Creating directory {} for the file {}".format(fildir,filename))


    if(not os.path.exists(filepath)) or (os.path.getsize(filepath)==0):
        with open(filepath,'w') as f:
            pass
            logging.info("Creating empty file:{}".format(filepath))
        
    else:
        logging.info("{} is already exists".format(filepath))
    