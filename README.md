# 🚀 **Genomics Analysis Demo: Code Ocean 101**
This repository is a starter kit designed for novice Code Ocean users. It simulates a standard genomics workflow—taking raw expression counts, performing a normalization, and generating a visual report.

## 🎯 Learning Objectives
By importing this repository into a Code Ocean capsule, you will learn:

+ Environment Setup: How requirements.txt automatically builds your compute environment.

+ Data Mounting: How files in /data are treated as read-only inputs.

+ Reproducibility: How the run script automates your entire analysis.

+ Results Persistence: How to ensure plots and tables are saved to the /results folder.

## 🛠 How to Use
1. Log in to Code Ocean.

2. Select "Create New Capsule" -> "Copy from GitHub".

3. Paste this repository URL.

4. From here, load your enviornment + packages.
5. Play around with the script by launching a **cloud workstation** or create a **Reproducible Run** by right clicking the script and selecting, "Set as the script to run".  


## 📊 About the Analysis
This demo utilizes a small, generic gene expression dataset (sample_expression.csv) to:

+ Perform a log-transformation (handling zeros with pseudocounts).
+ Calculate Mean Sample Expression vs. a Control group.
+ Generate a Gene Type Distribution bar chart using Seaborn and Matplotlib.
+ Validate the environment using Biopython for metadata checks.
