#Program: Power-Law (Gamma) Transformations
import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread('img.tif', cv2.IMREAD_GRAYSCALE)
#Normalize the image to the range [0, 1]
normalized_img = img / 255.0

# Apply gamma correction for 0 < gamma < 1
gamma_01 = 0.5  # Example gamma value for enhancement
gamma_img_01 = np.array(255 * normalized_img ** gamma_01, dtype=np.uint8)

# Apply gamma correction for gamma > 1
gamma_2 = 2.0  # Example gamma value for darkness enhancement
gamma_img_2 = np.array(255 * normalized_img ** gamma_2, dtype=np.uint8)

# Display the original and corrected images
plt.figure(figsize=(12, 6))

# Original image
plt.subplot(1, 3, 1)
plt.imshow(img, cmap='gray')
plt.title("Original Image")
plt.axis('off')

# Gamma correction (0 < gamma < 1)
plt.subplot(1, 3, 2)
plt.imshow(gamma_img_01, cmap='gray')
plt.title("Gamma (0 < gamma < 1)")
plt.axis('off')

# Gamma correction (gamma > 1)
plt.subplot(1, 3, 3)
plt.imshow(gamma_img_2, cmap='gray')
plt.title("Gamma (gamma > 1)")
plt.axis('off')

plt.show()

plt.pause(0.001)
plt.close('all')
