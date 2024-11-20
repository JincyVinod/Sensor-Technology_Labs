#Program: Median Filtering
import cv2
import matplotlib.pyplot as plt

# Step 1: Read the image
img = cv2.imread('peppersaltImg.tif', cv2.IMREAD_GRAYSCALE)

# Step 2: Apply Median Filter with kernel size 5
median_filtered_img = cv2.medianBlur(img, 5)

# Step 3: Display the original and filtered images
plt.figure(figsize=(10, 5))

# Original Image
plt.subplot(1, 2, 1)
plt.imshow(img, cmap='gray')
plt.title("Original Image (Salt-and-Pepper Noise)")
plt.axis('off')

# Median Filtered Image
plt.subplot(1, 2, 2)
plt.imshow(median_filtered_img, cmap='gray')
plt.title("Median Filtered Image")
plt.axis('off')

plt.show()

plt.pause(0.001)
plt.close('all')
