# Face Cropper for ID Photos

![Python](https://img.shields.io/badge/python-v3.7+-blue.svg)
![OpenCV](https://img.shields.io/badge/opencv-v4.0+-green.svg)
![License](https://img.shields.io/badge/license-MIT-blue.svg)

A robust Python-based tool that detects and crops frontal faces from images, specifically optimized for ID card and passport photo processing. The tool uses OpenCV's deep learning face detector to accurately identify faces, filter out partial or side-profile faces, and produce high-quality 720×720 pixel cropped images suitable for official documents.

## 🌟 Features

- **Advanced Face Detection**: Uses OpenCV's DNN-based face detector for high accuracy
- **Quality Filtering**: Automatically filters out partial faces, side profiles, and low-quality detections
- **Smart Cropping**: Crops faces with intelligent padding while maintaining aspect ratio
- **Batch Processing**: Process multiple images simultaneously from input folder
- **Standardized Output**: Resizes all cropped faces to 720×720 pixels (perfect for ID photos)
- **Easy Setup**: Simple Python script with minimal dependencies

## 📁 Project Structure

```
face-cropper/
├── img/                                      # Input images folder
├── crop_img/                                 # Output cropped faces folder
├── models/
│   ├── deploy.prototxt                       # Face detector configuration
│   └── res10_300x300_ssd_iter_140000.caffemodel  # Pre-trained weights
├── face_cropper.py                           # Main Python script
├── requirements.txt                          # Python dependencies
└── README.md                                 # This file
```

## 🚀 Quick Start

### Prerequisites

- Python 3.7 or higher
- pip package manager

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/face-cropper.git
   cd face-cropper
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Download required model files**

   **Option 1: Direct Download**
   - Download `res10_300x300_ssd_iter_140000.caffemodel` from [Hugging Face](https://huggingface.co/spaces/liangtian/birthdayCrown/blob/3db8f1c391e44bd9075b1c2854634f76c2ff46d0/res10_300x300_ssd_iter_140000.caffemodel)
   - Download `deploy.prototxt` from [Hugging Face](https://huggingface.co/spaces/OpenCVUniversity/face-detection-using-OpenCV/blob/main/deploy.prototxt)
   
   **Option 2: Using wget (Linux/Mac)**
   ```bash
   mkdir -p models
   cd models
   wget -O res10_300x300_ssd_iter_140000.caffemodel "https://huggingface.co/spaces/liangtian/birthdayCrown/resolve/main/res10_300x300_ssd_iter_140000.caffemodel"
   wget -O deploy.prototxt "https://huggingface.co/spaces/OpenCVUniversity/face-detection-using-OpenCV/raw/main/deploy.prototxt"
   cd ..
   ```

4. **Create necessary directories**
   ```bash
   mkdir -p img crop_img
   ```

5. **Add your images**
   - Place the images you want to process in the `img/` folder
   - Supported formats: `.jpg`, `.jpeg`, `.png`, `.bmp`, `.tiff`

### Usage

Run the face cropper:
```bash
python face_cropper.py
```

The script will automatically:
- ✅ Scan all images in the `img/` folder
- ✅ Detect faces using deep learning
- ✅ Filter out partial or side-profile faces
- ✅ Crop detected faces with appropriate padding
- ✅ Resize to 720×720 pixels
- ✅ Save results in the `crop_img/` folder


## ⚙️ Configuration

You can modify the following parameters in `face_cropper.py`:

```python
# Detection confidence threshold
CONFIDENCE_THRESHOLD = 0.5

# Output image size
OUTPUT_SIZE = (720, 720)

# Padding around detected face (as percentage)
PADDING_PERCENTAGE = 0.2
```

## 🛠️ Dependencies

- `opencv-python` >= 4.0.0
- `numpy` >= 1.19.0
- `Pillow` >= 8.0.0

Install all dependencies:
```bash
pip install opencv-python numpy Pillow
```

## 📝 Algorithm Details

1. **Face Detection**: Uses OpenCV's DNN module with a pre-trained SSD MobileNet model
2. **Quality Filtering**: 
   - Checks confidence score (>50%)
   - Validates aspect ratio (0.7-1.3 for frontal faces)
   - Ensures face is fully within image boundaries
3. **Cropping**: Adds 20% padding around detected face bounding box
4. **Resizing**: Uses high-quality interpolation to resize to 720×720 pixels

## 🔧 Troubleshooting

**Common Issues:**

- **No faces detected**: Ensure images have clear, front-facing faces with good lighting
- **Poor quality crops**: Try adjusting the `CONFIDENCE_THRESHOLD` parameter
- **Memory errors**: Process images in smaller batches or resize input images

**Error Messages:**
- `Model file not found`: Ensure model files are downloaded and in correct location
- `No input images found`: Check that images are in the `img/` folder

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request. For major changes, please open an issue first to discuss what you would like to change.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 👨‍💻 Author

**Sagar Hodar**
- 📧 Email: hodarsagar@gmail.com
- 🐙 GitHub: [@sagarhodar](https://github.com/sagarhodar)

## 🙏 Acknowledgments

- OpenCV community for providing excellent computer vision tools
- The creators of the SSD MobileNet face detection model
- Contributors and users who help improve this project

## 📈 Project Status

This project is actively maintained. If you encounter any issues or have suggestions for improvements, please feel free to open an issue or contact the author.

---

⭐ **If this project helped you, please give it a star!** ⭐
