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

### Approach

1. **Preprocessing**
   - Loaded multiple overlapping images from the `images` directory.
   - Converted images to grayscale for feature detection.
   
2. **Feature Detection and Matching**
   - Used ORB (Oriented FAST and Rotated BRIEF) to detect keypoints and descriptors in each image.
   - Saved images with detected keypoints for visualization.
   
3. **Panorama Stitching**
   - Used OpenCV's `Stitcher` to align and blend images into a seamless panorama.
   - If stitching succeeded, saved the final panorama image.
   
4. **Final Enhancements**
   - Detected and highlighted keypoints in the stitched panorama for better visualization.
   
### Output
- The stitched panorama is saved as `output/panorama.jpg`.
- Individual images with detected keypoints are saved as `output/keypoints_*.jpg`.
- The final panorama with keypoints is saved as `output/panorama_with_keypoints.jpg`.

### How to Run
#### Requirements
- Python 3
- OpenCV
- NumPy

#### Execution
Ensure the `images` directory contains the overlapping images to be stitched. Then, run:

```bash
python3 panaroma.py
```

This will save the stitched panorama and keypoint-visualized images in the `output` directory.

---

## Results and Observations

### Coin Detection and Segmentation
- Successfully detected and outlined coins in most cases.
- Performed well with clear, well-lit images but struggled with overlapping or shadowed coins.
- Watershed-based segmentation helped isolate individual coins effectively.

### Panorama Stitching
- Successfully stitched images with sufficient overlap and alignment.
- Worked best when images had distinct, well-distributed features.
- Failed when images had little overlap or significant distortion.


