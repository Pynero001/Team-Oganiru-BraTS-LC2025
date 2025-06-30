import os 
import subprocess

os.environ["nnUNet_raw"] = "/teamspace/studios/this_studio/nnUNet_raw"
os.environ["nnUNet_preprocessed"] = "/teamspace/studios/this_studio/nnUNet_preprocessed"
os.environ["nnUNet_results"] = "/teamspace/studios/this_studio/nnUNet_results"

# Create predictions of test dataset. 
# Ensure the configuration, no of epochs and the fold used during training are the same.
from datetime import datetime, timedelta
start = datetime.now() + timedelta(hours=1)
print("Start time:", start)

subprocess.run([
    "nnUNetv2_predict", "-i", "/teamspace/studios/this_studio/nnUNet_raw/Dataset025_MICCAI/imagesTs",
    "-o", "/teamspace/studios/this_studio/nnUNet_predictions_v2/", "-d", "025", "-c",
    "3d_fullres", "-tr", "nnUNetTrainer_85epochs", "-f", "all"
])


end = datetime.now() + timedelta(hours=1)
print("End time:", end)
print(f"Total time to generate predictions: {(end-start)}")

# Requires GPU but doesn't take a lot of time