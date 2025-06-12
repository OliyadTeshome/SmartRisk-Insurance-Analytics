#!/bin/bash

# Create necessary directories if they don't exist
mkdir -p data/raw
mkdir -p data/processed

# Initialize DVC if not already initialized
if [ ! -d .dvc ]; then
    dvc init
fi

# Add Google Drive remote if not already added
if ! dvc remote list | grep -q "gdrive"; then
    dvc remote add -d gdrive gdrive://root/insurance_data
fi

# Pull the data
dvc pull

# Verify the data exists
if [ -f "data/raw/insurance_data.csv" ]; then
    echo "✅ Data successfully downloaded to data/raw/insurance_data.csv"
else
    echo "❌ Error: Data file not found"
    exit 1
fi 