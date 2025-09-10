import cv2
import os
import numpy as np

# Paths
input_dir = 'img'
output_dir = 'crop_img'
os.makedirs(output_dir, exist_ok=True)

# Load DNN face detector
modelFile = "res10_300x300_ssd_iter_140000.caffemodel"
configFile = "deploy.prototxt"
net = cv2.dnn.readNetFromCaffe(configFile, modelFile)

# List image files
image_files = [f for f in os.listdir(input_dir) if f.lower().endswith(('.jpg', '.jpeg', '.png'))]

padding_ratio = 0.2  # 20% padding
confidence_threshold = 0.4              # Allow aspect ratio between 40% Accuracy
aspect_ratio_tolerance = 0.5            # Allow aspect ratio between 50% Margin

for img_file in image_files:
    image_path = os.path.join(input_dir, img_file)
    img = cv2.imread(image_path)
    if img is None:
        print(f"Failed to load {img_file}")
        continue

    h_img, w_img = img.shape[:2]
    blob = cv2.dnn.blobFromImage(cv2.resize(img, (300, 300)), 1.0,
                                 (300, 300), (104.0, 177.0, 123.0))
    net.setInput(blob)
    detections = net.forward()

    face_found = False

    for i in range(detections.shape[2]):
        confidence = detections[0, 0, i, 2]
        if confidence < confidence_threshold:
            continue

        box = detections[0, 0, i, 3:7] * np.array([w_img, h_img, w_img, h_img])
        (x1, y1, x2, y2) = box.astype("int")

        # Ensure box is fully inside the image
        if x1 < 0 or y1 < 0 or x2 > w_img or y2 > h_img:
            continue

        width = x2 - x1
        height = y2 - y1

        # Check aspect ratio
        aspect_ratio = width / float(height)
        if not (1 - aspect_ratio_tolerance <= aspect_ratio <= 1 + aspect_ratio_tolerance):
            continue

        # Passed all checks → good frontal face
        face_found = True

        # Apply padding
        cx = x1 + width // 2
        cy = y1 + height // 2
        size = int(max(width, height) * (1 + padding_ratio))
        x1_new = max(cx - size // 2, 0)
        y1_new = max(cy - size // 2, 0)
        x2_new = min(x1_new + size, w_img)
        y2_new = min(y1_new + size, h_img)
        x1_new = max(x2_new - size, 0)
        y1_new = max(y2_new - size, 0)

        face_img = img[y1_new:y2_new, x1_new:x2_new]
        face_img = cv2.resize(face_img, (720, 720))

        base_name = os.path.splitext(img_file)[0]
        cropped_face_path = os.path.join(output_dir, f"{base_name}_face{i+1}.jpg")
        cv2.imwrite(cropped_face_path, face_img)
        print(f"Cropped face saved as {cropped_face_path}")

    if not face_found:
        print(f"No good frontal face detected in {img_file}")



# You can further enhance by:

# Increasing confidence_threshold to be more strict.

# Adjusting aspect_ratio_tolerance for more or less strict frontal face checking.

# Adding checks for minimum face size to ensure it's suitable for ID photos.

# Let me know if you want to:

# Automate downloading the model files.

# Apply image enhancement after cropping.

# Use dlib or other advanced face detectors