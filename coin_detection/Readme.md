## Folder Structure
\`\`\`
coin_detection/
images/                 # Input images (coins)
output/                 # Output results (detection, segmentation, and counting)
coin_detection.py        # Script for processing
README.md                # Instructions
\`\`\`

## How to Run
1. Install dependencies:
   \`\`\`bash
   pip install opencv-python numpy
   \`\`\`
2. Place your coin image inside the \`images/\` folder.
3. Run the script:
   \`\`\`bash
   python coin_detection.py
   \`\`\`

4. Outputs:
   - \`output/detected_coins.jpg\` → Coins outlined after edge detection.
   - \`output/segmented_coins/\` → Individual segmented coins.
   - Console Output → Displays the **total number of coins** detected.

---

## Methods Used
✔ **Edge Detection (Canny Filter)** → Detects coin edges.  
✔ **Hough Circle Transform** → Detects circular shape for coins.  
✔ **Region-Based Segmentation** → Identifies individual coins.  
✔ **Counting Algorithm** → counts total coins detected.

---

## ❌ Common Issues
- **Detection is poor?** → Adjust \`Canny\` thresholds in the code.  
- **Wrong count?** → Check if coins are touching; use better lighting.