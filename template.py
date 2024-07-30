
import os 
from pathlib import Path
import logging

list = [
  ".github/workflows/.gitkeep",
  
  "src/__init__.py",
  "src/components/__init__.py",
  "src/components/data_ingestion.py",
  "src/components/data_validation.py",
  "src/components/model_trainer.py",
  
  "src/pipeline/__init__.py",
  "src/pipeline/training_pipeline.py",
  "src/pipeline/prediction_pipeline.py",
  
  "src/utils/__init__.py",
  "src/utils/utils.py",
  
  "src/logger/__init__.py",
  "src/exception/__init__.py"
  "src/logger/logging.py",
  "src/exception/exception.py",
  
  "templates/index.html",
  "app.py",
  
  "Dockerfile",
  
  "requirements.txt",
  "setup.py",
  "init_setup.sh",

  "experiment/trials.ipynb",
  
]

for filepath in list:
  filepath = Path(filepath)
  filedir,filename = os.path.split(filepath)
  
  if filedir!="":
    os.makedirs(filedir,exist_ok=True)
    # logging.info(f"Making the directory:{filedir} for the file: {filename}")
    
  if (not os.path.exists(filepath)) or (os.path.getsize(filepath)==0):
    with open(filepath,"w") as f:
      pass
      # logging.info(f"Creating empty file: {filename}")
  # else:
    # logging.info(f"{filename} is already created")
  
  
