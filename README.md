# Face Cropper for ID Photos

A simple Python-based tool to detect and crop frontal faces from images, optimized for ID card photos. It processes all images in the `img/` folder, detects faces that are fully visible and front-facing, crops them with padding, and resizes them to **720×720 pixels**, saving the results in the `crop_img/` folder.

## 📋 Features
- Uses OpenCV’s deep learning face detector for accurate frontal face detection.
- Filters out partial or side-profile faces by checking aspect ratio and bounding box boundaries.
- Automatically crops and resizes detected faces to 720×720 pixels suitable for ID cards.
- Processes multiple images in batch mode.
- Simple, easy-to-use Python script.

## 📂 File Structure
