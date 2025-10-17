import cv2
import numpy as np

# Load images
pattern = cv2.imread('Pattern.jpg')   # White cloth with stand
flag = cv2.imread('Flag.jpg')         # U.S. flag image

# Check loading
if pattern is None or flag is None:
    raise FileNotFoundError("Could not load Pattern.jpg or Flag.jpg. Check file paths.")

# Step 1: Resize flag to roughly match the cloth area
flag_resized = cv2.resize(flag, (pattern.shape[1], pattern.shape[0]))


 
# Step 2: Convert pattern to grayscale for shading reference
gray_pattern = cv2.cvtColor(pattern, cv2.COLOR_BGR2GRAY)
normalized = gray_pattern / 255.0  # Normalize shading

# Step 3: Apply brightness shading to flag based on cloth lighting
shaded_flag = cv2.convertScaleAbs(flag_resized * (0 + 0.5 * normalized[..., None]))

# Step 4: Create a perspective transform to fit flag naturally on cloth
rows, cols, _ = pattern.shape

# You can adjust these manually for better alignment if needed
pts1 = np.float32([[0, 0], [cols, 0], [0, rows], [cols, rows]])
pts2 = np.float32([
    [0, 0],          # top-left
    [cols - 0, 0],   # top-right
    [0, rows - 0],   # bottom-left
    [cols - 0, rows - 0]  # bottom-right
])

M = cv2.getPerspectiveTransform(pts1, pts2)
warped_flag = cv2.warpPerspective(shaded_flag, M, (cols, rows))

# Step 5: Blend warped flag with white cloth (Pattern)
final_output = cv2.addWeighted(warped_flag, 0.9, pattern, 0.2, 0)

# Save results
cv2.imwrite('Output.jpg', final_output)
cv2.imwrite('Warped_Flag.jpg', warped_flag)

print("Flag successfully placed and saved as Output.jpg")