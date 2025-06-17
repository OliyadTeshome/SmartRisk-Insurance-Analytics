# dvc_storage

This folder contains DVC-tracked files that represent the versioned data artifacts for the project. The `.dvc` files point to data stored remotely (e.g., on Google Drive) and are used to manage and reproduce data pipelines.

## Contents
- `cleaned_insurance_data.csv.dvc`: DVC file tracking the cleaned insurance dataset.
- `insurance_data.csv.dvc`: DVC file tracking the raw insurance dataset.

> **Note:** The actual data files are not stored in the repository, only the DVC metafiles. 