#Program: Averaging
import cv2
import matplotlib.pyplot as plt

# Step 1: Read the image (replace with your image paths as needed)
img = cv2.imread('peppersaltImg.tif', cv2.IMREAD_GRAYSCALE)

# Step 2: Apply the averaging filter with a 5x5 kernel
filtered_img_5x5 = cv2.blur(img, (5, 5))

# Step 3: Apply the averaging filter with a 3x3 kernel
filtered_img_3x3 = cv2.blur(img, (3, 3))

# Step 4: Display the original and filtered images
plt.figure(figsize=(15, 5))

# Original image
plt.subplot(1, 3, 1)
plt.imshow(img, cmap='gray')
plt.title("Original Image")
plt.axis('off')

# Filtered image (5x5 kernel)
plt.subplot(1, 3, 2)
plt.imshow(filtered_img_5x5, cmap='gray')
plt.title("Filtered (5x5 Kernel)")
plt.axis('off')

plt.subplot(1, 3, 3)
plt.imshow(filtered_img_3x3, cmap='gray')
plt.title("Filtered (3x3 Kernel)")
plt.axis('off')

plt.show()

plt.pause(0.001)
plt.close('all')