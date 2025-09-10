import cv2

# Load Haar cascade for face detection
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

# Load the image
image_path = 'input_image.jpg'  # Replace with your image path
img = cv2.imread(image_path)
height, width = img.shape[:2]

# Convert to grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Detect faces
faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5)

# Crop and resize each face
padding_ratio = 0.2  # 20% padding around the face

for i, (x, y, w, h) in enumerate(faces):
    # Find the center of the face
    cx, cy = x + w // 2, y + h // 2
    
    # Determine size of square crop
    size = int(max(w, h) * (1 + padding_ratio))
    
    # Calculate new top-left corner
    x1 = max(cx - size // 2, 0)
    y1 = max(cy - size // 2, 0)
    
    # Calculate bottom-right corner ensuring it's within image bounds
    x2 = min(x1 + size, width)
    y2 = min(y1 + size, height)
    
    # Adjust x1 and y1 if crop size is smaller at the edges
    x1 = max(x2 - size, 0)
    y1 = max(y2 - size, 0)
    
    # Crop the face region
    face_img = img[y1:y2, x1:x2]
    
    # Resize to 720x720 pixels
    face_img = cv2.resize(face_img, (720, 720))
    
    # Save the cropped and resized face
    cropped_face_path = f'cropped_face_{i+1}.jpg'
    cv2.imwrite(cropped_face_path, face_img)
    print(f"Cropped and resized face saved as {cropped_face_path}")
