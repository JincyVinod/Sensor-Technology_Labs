#Program: Image negatives
import cv2
import matplotlib.pyplot as plt


# Read the image
img = cv2.imread('img.tif', cv2.IMREAD_GRAYSCALE)

# Invert the image to obtain the negative of the image
new_img = cv2.bitwise_not(img)  #negative = 255-pixel

# Display the original and the negative image
plt.figure(figsize=(10, 5))

# Original image
plt.subplot(1, 2, 1)
plt.imshow(img, cmap='gray')
plt.title("Original Image")
plt.axis('off')

# Negative image
plt.subplot(1, 2, 2)
plt.imshow(new_img, cmap='gray')
plt.title("Negative Image")
plt.axis('off')

plt.show()

plt.pause(0.001)
plt.close('all')

