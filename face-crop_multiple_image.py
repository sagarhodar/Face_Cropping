import cv2
import os

# Create output directory if it doesn't exist
input_dir = 'img'
output_dir = 'crop_img'
os.makedirs(output_dir, exist_ok=True)

# Load Haar cascade for face detection
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

# List all image files in input directory
image_files = [f for f in os.listdir(input_dir) if f.lower().endswith(('.jpg', '.jpeg', '.png'))]

padding_ratio = 0.2  # 20% padding around the face

for img_file in image_files:
    image_path = os.path.join(input_dir, img_file)
    img = cv2.imread(image_path)
    if img is None:
        print(f"Failed to load {img_file}")
        continue
    
    height, width = img.shape[:2]
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5)

    if len(faces) == 0:
        print(f"No face detected in {img_file}")
        continue

    for i, (x, y, w, h) in enumerate(faces):
        cx, cy = x + w // 2, y + h // 2
        size = int(max(w, h) * (1 + padding_ratio))
        x1 = max(cx - size // 2, 0)
        y1 = max(cy - size // 2, 0)
        x2 = min(x1 + size, width)
        y2 = min(y1 + size, height)
        x1 = max(x2 - size, 0)
        y1 = max(y2 - size, 0)
        
        face_img = img[y1:y2, x1:x2]
        face_img = cv2.resize(face_img, (720, 720))

        base_name = os.path.splitext(img_file)[0]
        cropped_face_path = os.path.join(output_dir, f"{base_name}_face{i+1}.jpg")
        cv2.imwrite(cropped_face_path, face_img)
        print(f"Cropped face saved as {cropped_face_path}")
