#Program: Log Transformations
import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread('img.tif', cv2.IMREAD_GRAYSCALE)
#S = c * log (1 + r)
#r = input pixel value
#S = output pixel value

# Step 2: finding the maximum pixel value in the image
m = np.max(img)
print("Maximum pixel value in the image:", m)

# Step 3: Handle potential issues with maximum pixel value
if m == 0:  # Avoid log(1 + 0)
    c = 0
else:
    # c = scaling constant, can be given by 255/(log (1 + m)), where m is the maximum pixel value in the image.
    c = 255 / (np.log(1 + m + 1e-10))  # Add small constant to avoid divide by zero

# Step 4: Apply log transformation
log_transformed = c * np.log(1 + img.astype(np.float32))

# Step 5: Normalize the transformed image
log_transformed = np.uint8(cv2.normalize(log_transformed, None, 0, 255, cv2.NORM_MINMAX))

# Step 6: Display the original and transformed images
plt.figure(figsize=(10, 5))

# Original image
plt.subplot(1, 2, 1)
plt.imshow(img, cmap='gray')
plt.title("Original Image")
plt.axis('off')

# Log-transformed image
plt.subplot(1, 2, 2)
plt.imshow(log_transformed, cmap='gray')
plt.title("Log-Transformed Image")
plt.axis('off')

plt.show()

plt.pause(0.001)
plt.close('all')