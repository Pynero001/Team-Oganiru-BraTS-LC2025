# Team-Oganiru-BraTS-LC2025

# Brain Tumor Segmentation with nnU-Net (BraTS Lighthouse Challenge)

This repository contains Team Nigeria South East - Oganiru solutions for the **BraTS Lighthouse Challenge**, where the objective is to segment brain tumors from multi-modal MRI scans.

The project explores **deep learning–based medical image segmentation** using **nnU-Net**.

The workflow includes:

* MRI dataset preprocessing
* nnU-Net training pipeline
* Evaluation using standard medical segmentation metrics

---

# Project Overview

Brain tumor segmentation is important for **treatment planning, monitoring disease progression, and surgical guidance**.

The BraTS dataset contains **multi-modal MRI scans**, including:

* T1
* T1c (contrast-enhanced)
* T2
* FLAIR

The goal is to segment tumor subregions:

* Enhancing Tumor (ET)
* Tumor Core (TC)
* Whole Tumor (WT)

---

# Model Architecture

## nnU-Net

nnU-Net is a **self-configuring biomedical segmentation framework** that automatically determines:

* preprocessing strategies
* patch size
* batch size
* network architecture
* training schedules

It is widely regarded as one of the strongest baseline models for biomedical segmentation tasks.

# Dataset

The project uses the **BraTS Sub-Saharan Africa (SSA) dataset**, which contains:

* Multi-modal 3D MRI volumes
* Expert-annotated tumor segmentation masks

Each case includes:

```
Patient_ID/
 ├── T1.nii.gz
 ├── T1c.nii.gz
 ├── T2.nii.gz
 ├── FLAIR.nii.gz
 └── segmentation_mask.nii.gz
```

---

# Training Pipeline

The training workflow includes:

1. Dataset preprocessing
2. nnU-Net dataset formatting
3. Model training
4. Validation monitoring
5. Model checkpointing
6. Final inference

---

# Evaluation Metrics

Performance is evaluated using standard **medical image segmentation metrics**.

**NB**: The original nnUNet was forked and modified to enable HD95 score as an evaluation metric.

## Dice Score

Measures spatial overlap between predicted segmentation and ground truth.

```
Dice = 2|A ∩ B| / (|A| + |B|)
```

---

## Hausdorff Distance (HD95)

Measures the **95th percentile distance between prediction and ground truth boundaries**, which reflects segmentation boundary accuracy.

---

Key libraries:

* PyTorch
* MONAI
* medpy
* numpy
  

# Acknowledgements

* SPARK Academy
* BraTS Challenge organizers
* nnU-Net developers

---

