import os
from glob import glob
import shutil
import numpy as np


directory = "/teamspace/studios/this_studio/BraTS_Train/ASNR-MICCAI-BraTS2023-SSA-Challenge-TrainingData_V2"
img_path = sorted(glob(os.path.join(directory, "**", "*t*nii.gz"), recursive=True))
sm_paths = sorted(glob(os.path.join(directory, "**", "*seg*nii.gz")))
os.makedirs("/teamspace/studios/this_studio/nnUNet_raw", exist_ok=True)
os.makedirs("/teamspace/studios/this_studio/nnUNet_preprocessed", exist_ok=True)
os.makedirs("/teamspace/studios/this_studio/nnUNet_results", exist_ok=True)

os.environ["nnUNet_raw"] = "/teamspace/studios/this_studio/nnUNet_raw"
os.environ["nnUNet_preprocessed"] = "/teamspace/studios/this_studio/nnUNet_preprocessed"
os.environ["nnUNet_results"] = "/teamspace/studios/this_studio/nnUNet_results"
# Task/Dataset name must be written as "DatasetXXX_YYY", where XXX reps numbers from 000-999 and YYY, your custom title
task_name = "Dataset025_MICCAI"
task_dir = f"{os.environ['nnUNet_raw']}/{task_name}"

# Create folders
os.makedirs(f"{task_dir}/imagesTr", exist_ok=True)  
os.makedirs(f"{task_dir}/labelsTr", exist_ok=True)
os.makedirs(f"{task_dir}/imagesTs", exist_ok=True) 
os.makedirs(f"{task_dir}/labelsTs", exist_ok=True) 
train_modality_mapping = {"t1n": 0, "t2w": 1, "t1c": 2, "t2f": 3, "seg":4}
test_modality_mapping = {"t1n": 0, "t2w": 1, "t1c": 2, "t2f": 3}

train_scans_dir = "/teamspace/studios/this_studio/BraTS_Train/ASNR-MICCAI-BraTS2023-SSA-Challenge-TrainingData_V2/"
test_scans_dir = "/teamspace/studios/this_studio/BraTS_Val/BraTS2024-SSA-Challenge-ValidationData/"

train_mri_scans = [d for d in os.listdir(train_scans_dir) if os.path.isdir(f"{train_scans_dir}/{d}")]
test_mri_scans = [d for d in os.listdir(test_scans_dir) if os.path.isdir(f"{test_scans_dir}/{d}")]

for train_scan in train_mri_scans:
    for modality, channel in train_modality_mapping.items():
        if modality == "seg":
            input_file = f"{train_scans_dir}{train_scan}/{train_scan}-{modality}.nii.gz"
            output_file = f"{task_dir}/labelsTr/{train_scan}.nii.gz"
            shutil.copy(input_file, output_file)
        else:
            input_file = f"{train_scans_dir}{train_scan}/{train_scan}-{modality}.nii.gz"
            output_file = f"{task_dir}/imagesTr/{train_scan}_{str(channel).zfill(4)}.nii.gz"
            shutil.copy(input_file, output_file)

for test_scan in test_mri_scans:
    for modality, channel in test_modality_mapping.items():
        input_file = f"{test_scans_dir}{test_scan}/{test_scan}-{modality}.nii.gz"
        output_file = f"{task_dir}/imagesTs/{test_scan}_{str(channel).zfill(4)}.nii.gz"
        shutil.copy(input_file, output_file)
