# Face Cropper for ID Photos

A simple Python-based tool to detect and crop frontal faces from images, optimized for ID card photos. It processes all images in the `img/` folder, detects faces that are fully visible and front-facing, crops them with padding, and resizes them to **720×720 pixels**, saving the results in the `crop_img/` folder.

## 📋 Features
- Uses OpenCV’s deep learning face detector for accurate frontal face detection.
- Filters out partial or side-profile faces by checking aspect ratio and bounding box boundaries.
- Automatically crops and resizes detected faces to 720×720 pixels suitable for ID cards.
- Processes multiple images in batch mode.
- Simple, easy-to-use Python script.

## 📂 File Structure

/your_project_directory

img/ # Input images folder
crop_img/ # Output cropped images folder
deploy.prototxt # Face detector configuration file
res10_300x300_ssd_iter_140000.caffemodel # Pre-trained model weights
face_cropper.py # Main Python script
README.md # Project documentation



---

## ✅ Step 1: Download the Required Files

### 📥 Model Weights  
**`res10_300x300_ssd_iter_140000.caffemodel`**  
You can download the model weights from this link:  
[Download from Hugging Face](https://huggingface.co/spaces/liangtian/birthdayCrown/blob/3db8f1c391e44bd9075b1c2854634f76c2ff46d0/res10_300x300_ssd_iter_140000.caffemodel?utm_source=chatgpt.com)

### 📥 Configuration File  
**`deploy.prototxt`**  
Download the configuration file from this link:  
[Download from Hugging Face](https://huggingface.co/spaces/OpenCVUniversity/face-detection-using-OpenCV/blob/main/deploy.prototxt?utm_source=chatgpt.com)

---

## ✅ Step 2: Prepare Your Project Directory



mkdir img crop_img

Add the images you want to process in the img/ folder.


## ✅ Step 3: Run the Python Script
With everything set up, you can run the script using:

bash

python face_cropper.py


The script will:
✔ Detect faces in each image
✔ Verify that the face is fully visible and front-facing
✔ Crop the face with padding
✔ Resize it to 720×720 pixels
✔ Save the result in the crop_img/ folder

📧 Contact
For any questions, suggestions, or feedback, feel free to contact:

Sagar Hodar
✉ hodarsagar@gmail.com

📜 Credits
This project uses the OpenCV library and the publicly available deep learning face detector model from OpenCV’s samples. Special thanks to the OpenCV community for providing open-source tools and models that make computer vision accessible to everyone.

📄 License
Feel free to use and modify this project for educational or personal purposes. Please acknowledge the source if you share or publish your work.

