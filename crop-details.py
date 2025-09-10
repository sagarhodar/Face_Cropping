import cv2
import os
import csv

# Set paths
input_dir = 'crop_img'
csv_file = 'crop_img.csv'

# List all image files in the directory
image_files = [f for f in os.listdir(input_dir) if f.lower().endswith(('.jpg', '.jpeg', '.png'))]

# Open CSV file for writing
with open(csv_file, mode='w', newline='') as file:
    writer = csv.writer(file)
    
    # Write header row
    writer.writerow(['Image Name', 'Extension', 'Height', 'Width', 'Size (bytes)', 'Format', 'Channels'])
    
    for img_file in image_files:
        image_path = os.path.join(input_dir, img_file)
        
        # Get file size
        size_bytes = os.path.getsize(image_path)
        
        # Load image to get properties
        img = cv2.imread(image_path)
        if img is None:
            print(f"Failed to load {img_file}")
            continue
        
        height, width = img.shape[:2]
        channels = img.shape[2] if len(img.shape) == 3 else 1
        extension = os.path.splitext(img_file)[1].lower()
        
        # OpenCV doesn't retain original format, but extension is a good hint
        img_format = extension.replace('.', '').upper()
        
        # Write row to CSV
        writer.writerow([img_file, extension, height, width, size_bytes, img_format, channels])

print(f"Image specs have been saved to {csv_file}")
