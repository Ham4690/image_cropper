#!/bin/bash

# Simple script to run the image cropper tool

# Path to the input and output directory
INPUT_DIR="images/input"
OUTPUT_DIR="images/output"

# Desired size
SIZE="1535x1024"

# Find all images in $INPUT_DIR and crop them
for image in $INPUT_DIR/*; do
    # Extract filename
    filename=$(basename -- "$image")
    # Run the cropper tool
    python3 -m image_cropper.main "$image" "$OUTPUT_DIR/$filename" $SIZE
done

echo "Image cropping complete!"
