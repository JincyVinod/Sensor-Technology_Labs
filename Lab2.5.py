#Program: Gaussian Filter
import cv2
import matplotlib.pyplot as plt

# Step 1: Read the image (replace with your image paths)
img = cv2.imread('peppersaltImg.tif', cv2.IMREAD_GRAYSCALE)

# Step 2: Apply Gaussian filter with a 5x5 kernel
gaussian_filtered_img = cv2.GaussianBlur(img, (5, 5), 0)

# Step 3: Display the original and filtered images
plt.figure(figsize=(10, 5))

# Original image
plt.subplot(1, 2, 1)
plt.imshow(img, cmap='gray')
plt.title("Original Image")
plt.axis('off')

# Gaussian Filtered image
plt.subplot(1, 2, 2)
plt.imshow(gaussian_filtered_img, cmap='gray')
plt.title("Gaussian Filtered Image (5x5 Kernel)")
plt.axis('off')

plt.show()

plt.pause(0.001)
plt.close('all')