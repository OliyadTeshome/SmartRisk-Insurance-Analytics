#!/usr/bin/env python3
import os
import subprocess
from pathlib import Path
import gdown

def download_file():
    """Download the file from Google Drive using gdown."""
    # Create necessary directories
    Path("data/raw").mkdir(parents=True, exist_ok=True)
    Path("data/processed").mkdir(parents=True, exist_ok=True)
    
    # Google Drive file ID
    file_id = "1DuX5m_UsWzMR4kAelYPf1lD538_xjp_m"
    output_path = "data/raw/insurance_data.csv"
    
    # Download the file
    url = f"https://drive.google.com/uc?id={file_id}"
    try:
        gdown.download(url, output_path, quiet=False)
        print(f"✅ Data successfully downloaded to {output_path}")
        return True
    except Exception as e:
        print(f"❌ Error downloading file: {str(e)}")
        return False

def verify_data():
    """Verify that the data file exists."""
    data_path = Path("data/raw/insurance_data.csv")
    if data_path.exists():
        print(f"✅ Data file exists at {data_path}")
        return True
    else:
        print("❌ Error: Data file not found")
        return False

if __name__ == "__main__":
    try:
        if download_file():
            verify_data()
    except Exception as e:
        print(f"❌ Error: {str(e)}")
        exit(1) 