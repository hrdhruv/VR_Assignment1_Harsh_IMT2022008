# VR_Assignment1_Harsh_IMT2022008

## Part 1: Detecting, Segmenting, and Counting Coins using Computer Vision

### Approach

1. **Preprocessing**
   - Loaded the input image and converted it to grayscale.
   - Applied Gaussian blurring to reduce noise and smooth the image.
   
2. **Edge Detection**
   - Used Canny edge detection to identify the edges of the coins in the image.
   
3. **Coin Detection**
   - Applied Hough Circle Transform to detect circular shapes corresponding to coins.
   - Outlined detected coins using green circles and marked their centers in red.
   
4. **Segmentation**
   - Used thresholding and morphological operations to segment the coins.
   - Applied the Watershed algorithm to isolate individual coins.
   
5. **Counting Coins**
   - Counted the number of detected coins and printed the total count.
   
### Output
- The processed image with detected coins outlined is saved as `output/detected_coins.jpg`.
- The segmented image highlighting individual coins is saved as `output/segmented_coins.jpg`.
- The total count of detected coins is displayed on the terminal.

### How to Run
#### Requirements
- Python 3
- OpenCV
- NumPy

#### Execution
Ensure the `images` directory contains the input images. To run the coin detection script, use:

```bash
python3 coin_detection.py
```

This will save the outlined and segmented coin images in the `output` directory and display the total coin count.

---

## Part 2: Creating a Stitched Panorama from Overlapping Images

# Panorama Stitching using OpenCV

## Overview
This project implements an **image stitching algorithm** using **SIFT feature matching** and **homography estimation** to create a panorama from multiple images. It detects keypoints, matches features, aligns images, and blends them together to form a seamless stitched output.

## Features
- Extracts **SIFT features** from images.
- Uses **BFMatcher with Lowe’s ratio test** for keypoint matching.
- Computes **homography using RANSAC** to align images.
- Warps images using **cv2.warpPerspective**.
- Removes **black borders** for a clean output.
- Supports **visualization of matched keypoints**.

## Requirements
Ensure you have the following installed:
```bash
pip install opencv-python numpy
```

## Usage
### 1. Prepare Input Images
- Place multiple overlapping images inside the `input/` directory.
- Images should be numbered sequentially (e.g., `1.jpg`, `2.jpg`, `3.jpg`).

### 2. Run the Script
Execute the following command:
```bash
python panorama.py
```

### 3. View Output
- The stitched panorama will be saved in the `output/` directory as `final_panorama.jpg`.
- If visualization is enabled, intermediate match images will also be saved.

## Code Explanation
### `extract_features(img)`
Extracts **SIFT keypoints** and descriptors from the given image.

### `find_correspondences(kp1, kp2, des1, des2, ratio_thresh, ransac_thresh)`
Finds matching keypoints using **BFMatcher** and computes **homography matrix**.

### `stitch_images(image_list, match_ratio, ransac_thresh, visualize)`
Aligns and stitches two images together based on their keypoint matches.

### `generate_panorama(source_folder, save_folder, target_width, match_ratio, ransac_thresh, visualize)`
Processes multiple images, stitches them sequentially, and saves the final panorama.

## Notes
- The input images should have **significant overlapping regions** for better stitching.
- The script assumes images are named numerically (e.g., `1.jpg`, `2.jpg`).
- For better results, images should have consistent **lighting and perspective**.


## Results and Observations

### Coin Detection and Segmentation
- Successfully detected and outlined coins in most cases.
- Performed well with clear, well-lit images but struggled with overlapping or shadowed coins.
- Watershed-based segmentation helped isolate individual coins effectively.

### Panorama Stitching
- Successfully stitched images with sufficient overlap and alignment.
- Worked best when images had distinct, well-distributed features.
- Failed when images had little overlap or significant distortion.


