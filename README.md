# Face Cropper for ID Photos

A simple Python-based tool to detect and crop frontal faces from images, optimized for ID card photos. It processes all images in the `img/` folder, detects faces that are fully visible and front-facing, crops them with padding, and resizes them to **720×720 pixels**, saving the results in the `crop_img/` folder.

## 📋 Features
- Uses OpenCV’s deep learning face detector for accurate frontal face detection.
- Filters out partial or side-profile faces by checking aspect ratio and bounding box boundaries.
- Automatically crops and resizes detected faces to 720×720 pixels suitable for ID cards.
- Processes multiple images in batch mode.
- Simple, easy-to-use Python script.

## 📂 File Structure
------------------------------------------------------------------------


✅ Step 1: Download the Required Files

Model Weights (res10_300x300_ssd_iter_140000.caffemodel):

You can download the model weights from Hugging Face
.

Configuration File (deploy.prototxt):
https://huggingface.co/spaces/liangtian/birthdayCrown/blob/3db8f1c391e44bd9075b1c2854634f76c2ff46d0/res10_300x300_ssd_iter_140000.caffemodel?utm_source=chatgpt.com
https://huggingface.co/spaces/OpenCVUniversity/face-detection-using-OpenCV/blob/main/deploy.prototxt?utm_source=chatgpt.com
Download the configuration file from Hugging Face
.

✅ Step 2: Prepare Your Project Directory

Ensure your project directory has the following structure:

/your_project_directory
├── img/                    # Input images
├── crop_img/               # Output cropped images
├── deploy.prototxt         # Downloaded configuration file
└── res10_300x300_ssd_iter_140000.caffemodel  # Downloaded model weights

✅ Step 3: Use the Provided Python Script

With the necessary files in place, you can use the previously provided Python script to perform face detection and cropping. This script utilizes OpenCV's DNN module to detect faces in images located in the img/ folder and saves the cropped faces as 720x720 pixel images in the crop_img/ folder.

If you encounter any issues or need further assistance with setting up the environment or running the script, feel free to ask!
