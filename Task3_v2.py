import os
import subprocess


# Set paths. Do not change the directory names!
os.makedirs("/teamspace/studios/this_studio/nnUNet_raw", exist_ok=True)
os.makedirs("/teamspace/studios/this_studio/nnUNet_preprocessed", exist_ok=True)
os.makedirs("/teamspace/studios/this_studio/nnUNet_results", exist_ok=True)

os.environ["nnUNet_raw"] = "/teamspace/studios/this_studio/nnUNet_raw"
os.environ["nnUNet_preprocessed"] = "/teamspace/studios/this_studio/nnUNet_preprocessed"
os.environ["nnUNet_results"] = "/teamspace/studios/this_studio/nnUNet_results"


# Ensure the number after -d is available in your Dataset name eg. Dataset001_BrainMRI
from datetime import datetime, timedelta
start = datetime.now() + timedelta(hours=1)
print("Start time:", start)

subprocess.run([
    "nnUNetv2_plan_and_preprocess", "-d", "025", "-c", "3d_fullres",
     "--verify_dataset_integrity", "-np", "1" 
])

end = datetime.now() + timedelta(hours=1)
print("End time:", end)
print(f"Total planning and preprocessing time: {(end-start)}")

# To run scripts concurrently: python script1.py && python script2.py  
# Can be run on CPU 