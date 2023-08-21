import os
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO,
format="[ %(asctime)s ] %(lineno)d %(name)s - %(levelname)s - %(message)s",)



project_name="Text Summarizer"

list_of_files=[
    ".github/workflows/.gitkeep",
    f"SRC/{project_name}/__init__.py",
    f"SRC/{project_name}/components/__init__.py",
    f"SRC/{project_name}/utils/__init__.py",
    f"SRC/{project_name}/utils/common.py",
    f"SRC/{project_name}/logging/__init__.py",
    f"SRC/{project_name}/config/__init__.py",
    f"SRC/{project_name}/config/configuration.py",
    f"SRC/{project_name}/entity/__init__.py",
    f"SRC/{project_name}/pipeline/__init__.py",
    f"SRC/{project_name}/constant/__init__.py",
    "config/config.yaml",
    "params.yaml",
    "app.py",
    "main.py",
    "Dockerfile",
    "requirements.txt",
    "setup.py",
    "research/trials.ipynb"

]

for file_path in list_of_files:
    file_path = Path(file_path)
    file_dir,file_name=os.path.split(file_path)

    if file_dir != "":
        os.makedirs(file_dir,exist_ok=True)
        logging.info(f"directory created name={file_dir}")

    if (not os.path.exists(file_path)) or (os.path.getsize(file_path)==0):
        with open(file_path,'w') as f:
            pass
            logging.info(f"creating empty  file :{file_path}")

    else:
        logging.info(f"{file_name} already exits")