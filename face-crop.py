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

# Crop each face as a square, slightly bigger
padding = 60  # pixels to enlarge the crop area around the face

for i, (x, y, w, h) in enumerate(faces):
    # Find the center of the face
    cx, cy = x + w // 2, y + h // 2
    
    # The size of the square crop is the max of width and height plus padding
    size = max(w, h) + padding
    
    # Calculate new top-left corner
    x1 = max(cx - size // 2, 0)
    y1 = max(cy - size // 2, 0)
    
    # Ensure the square doesn't go out of image boundaries
    x2 = min(x1 + size, width)
    y2 = min(y1 + size, height)
    
    # Crop the face region
    face_img = img[y1:y2, x1:x2]
    
    # Save the cropped face
    cropped_face_path = f'cropped_face_{i+1}.jpg'
    cv2.imwrite(cropped_face_path, face_img)
    print(f"Cropped face saved as {cropped_face_path}")
