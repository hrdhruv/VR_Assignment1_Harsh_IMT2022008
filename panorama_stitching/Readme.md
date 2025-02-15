## Overview
This script stitches multiple overlapping images into a **single panoramic image** using OpenCV’s \`cv2.Stitcher_create()\`.

## Folder Structure
\`\`\`
panorama_stitching/
images/                 # Input images (overlapping photos)
output/                 # Final stitched panorama
panorama_stitching.py    # Python script for stitching
README.md                # Instructions
\`\`\`

## How to Run
1. Install dependencies:
   \`\`\`bash
   pip install opencv-python numpy
   \`\`\`
2. Place **6 overlapping images** inside the \`images/\` folder.  
   - Ensure **at least 30% overlap** between consecutive images.
   - Name them \`img1.jpg, img2.jpg, ..., img6.jpg\`.
   
3. Run the script:
   \`\`\`bash
   python panorama_stitching.py
   \`\`\`

4. Outputs:
   - \`output/panorama.jpg\` → Final stitched panorama.

---

## Methods Used
✔ **Feature Detection (Automatic in OpenCV Stitcher)** → Detects and matches key points automatically..  
✔ **Homography Estimation** → Computes transformations to align overlapping images.  
✔ **Image Warping & Transformation** → Warps images to correct perspective distortions. 
✔ **Image Blending** → Smoothly blends images.

---

## Common Issues
- **Stitching failed?** → Ensure good **overlap** and avoid moving objects.  
- **Distorted output?** → Try different lighting conditions.

