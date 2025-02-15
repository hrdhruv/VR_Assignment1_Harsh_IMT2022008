import cv2
import os

# Folder containing images
image_folder = "images"

# List of image filenames (Make sure they are in the correct order)
image_files = ["img1.jpeg", "img2.jpeg", "img3.jpeg", "img4.jpeg", "img5.jpeg", "img6.jpeg"]

# Load images
images = []
for filename in image_files:
    img_path = os.path.join(image_folder, filename)
    img = cv2.imread(img_path)
    if img is None:
        print(f"Error loading {filename}. Make sure the file exists and is a valid image.")
        continue
    images.append(img)

# Check if we have at least 2 images
if len(images) < 2:
    print("Error: Need at least 2 images to stitch a panorama!")
    exit()

# Create OpenCV Stitcher
stitcher = cv2.Stitcher_create()

# Stitch images
status, panorama = stitcher.stitch(images)

if status == cv2.Stitcher_OK:
    # Save and display the final panorama
    output_path = "output/panorama.jpg"
    cv2.imwrite(output_path, panorama)
    print(f"Panorama stitching completed! Saved at {output_path}")
else:
    print("Error: Panorama stitching failed!")


