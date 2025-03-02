import os
import cv2
import numpy as np

# Extract SIFT features from an image
def extract_features(img):
    sift = cv2.SIFT_create()
    key_pts, desc = sift.detectAndCompute(img, None)
    if not key_pts:
        return np.array([], dtype=np.float32), None
    key_pts = np.array([kp.pt for kp in key_pts], dtype=np.float32)
    return key_pts, desc

# Find matching keypoints using feature descriptors
def find_correspondences(kp1, kp2, des1, des2, ratio_thresh=0.75, ransac_thresh=5.0):
    if des1 is None or des2 is None:
        print("[ERROR] One or both images have no descriptors.")
        return None, None, None
    matcher = cv2.BFMatcher()
    matches = matcher.knnMatch(des1, des2, k=2)
    # Apply Lowe’s ratio test
    valid_matches = [(m.trainIdx, m.queryIdx) for m, n in matches if m.distance < ratio_thresh * n.distance]
    if len(valid_matches) < 4:
        print("[ERROR] Not enough matches found.")
        return None, None, None
    indices_2, indices_1 = zip(*valid_matches)
    pts1 = np.float32([kp1[i] for i in indices_1])
    pts2 = np.float32([kp2[i] for i in indices_2])
    # Compute homography using RANSAC
    H, mask = cv2.findHomography(pts1, pts2, cv2.RANSAC, ransac_thresh)
    if H is None:
        print("[ERROR] Homography computation failed.")
        return None, None, None
    return valid_matches, H, mask

# Visualize matching keypoints between two images
def visualize_matches(img1, img2, kp1, kp2, matches, mask=None):
    keypoints1 = [cv2.KeyPoint(x, y, 1) for (x, y) in kp1]
    keypoints2 = [cv2.KeyPoint(x, y, 1) for (x, y) in kp2]
    dmatches = [cv2.DMatch(_queryIdx=q, _trainIdx=t, _distance=0) for t, q in matches]    
    if mask is not None:
        mask = mask.ravel().tolist()
    return cv2.drawMatches(img1, keypoints1, img2, keypoints2, dmatches, None, matchColor=(0, 255, 0), matchesMask=mask, flags=2)

# Crop black borders after image warping
def remove_black_borders(img):
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    mask = cv2.threshold(gray, 1, 255, cv2.THRESH_BINARY)[1]
    coords = cv2.findNonZero(mask)
    if coords is not None:
        x, y, w, h = cv2.boundingRect(coords)
        return img[y:y + h, x:x + w]
    return img

# Stitch two images together
def stitch_images(image_list, match_ratio=0.75, ransac_thresh=4.0, visualize=False):
    img2, img1 = image_list  # Order: img2 (base), img1 (to be warped)
    key1, des1 = extract_features(img1)
    key2, des2 = extract_features(img2)
    match_data = find_correspondences(key1, key2, des1, des2, match_ratio, ransac_thresh)
    if not match_data:
        print("[ERROR] Insufficient matches found. Skipping image.")
        return None
    matches, H, mask = match_data
    # Warp img1 to align with img2
    panorama = cv2.warpPerspective(img1, H, (img1.shape[1] + img2.shape[1], img1.shape[0]))
    # Overlay img2 onto the stitched image
    panorama[0:img2.shape[0], 0:img2.shape[1]] = img2
    # Remove black borders
    panorama = remove_black_borders(panorama)
    if visualize:
        match_img = visualize_matches(img1, img2, key1, key2, matches, mask)
        return panorama, match_img
    return panorama

def generate_panorama(source_folder, save_folder, target_width=600, match_ratio=0.75, ransac_thresh=4.0, visualize=True):
    # Ensure source folder exists
    if not os.path.exists(source_folder):
        print(f"[ERROR] Input folder '{source_folder}' does not exist.")
        return
    # Collect and sort image paths
    img_paths = sorted([os.path.join(source_folder, f) for f in os.listdir(source_folder)],key=lambda x: int(os.path.splitext(os.path.basename(x))[0]))  
    if len(img_paths) < 2:
        print("[ERROR] At least two images are required to create a panorama.")
        return
    # Load and scale the first image
    def load_and_scale(image_path):
        img = cv2.imread(image_path)
        if img is None:
            print(f"[ERROR] Could not load image {image_path}. Skipping...")
            return None
        h, w = img.shape[:2]
        scale_factor = target_width / float(w)
        return cv2.resize(img, (target_width, int(h * scale_factor)), interpolation=cv2.INTER_AREA)
    base_img = load_and_scale(img_paths[0])
    if base_img is None:
        return  # Abort if the first image is missing
    for idx in range(1, len(img_paths)):
        next_img = load_and_scale(img_paths[idx])
        if next_img is None:
            continue  # Skip missing images
        # Stitch images
        stitched_result = stitch_images([base_img, next_img], match_ratio, ransac_thresh, visualize)
        if stitched_result:
            base_img, match_vis = stitched_result
            if visualize:
                cv2.imwrite(os.path.join(save_folder, f"match_{idx}.jpg"), match_vis)
    # Save final panorama
    cv2.imwrite(os.path.join(save_folder, "final_panorama.jpg"), base_img)
    print(f"Panorama successfully created and saved to {save_folder}.")

if __name__ == "__main__":
    os.makedirs("output", exist_ok=True)
    generate_panorama("input", "output")
