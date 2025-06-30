import os 
import subprocess

os.environ["nnUNet_raw"] = "/teamspace/studios/this_studio/nnUNet_raw"
os.environ["nnUNet_preprocessed"] = "/teamspace/studios/this_studio/nnUNet_preprocessed"
os.environ["nnUNet_results"] = "/teamspace/studios/this_studio/nnUNet_results"

# torch.compile() calls Triton, which requires CUDA ≥ 7.0.
# Kaggle's Tesla P100 is unsupported, so disable it with TORCHDYNAMO_DISABLE=1.
from datetime import datetime, timedelta
start = datetime.now() + timedelta(hours=1)
print("Start time:", start)

subprocess.run([
    "nnUNetv2_train", "025", "3d_fullres", "all", "-tr", "nnUNetTrainer_85epochs", "--c"
])


end = datetime.now() + timedelta(hours=1)
print("End time:", end)
print(f"Total training time: {(end-start)}")

#Run in terminal: python brats_preprocess.py && python brats_train.py   
# Never use interruptible GPUs here 

