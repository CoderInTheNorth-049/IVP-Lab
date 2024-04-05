import cv2
import numpy as np
import matplotlib.pyplot as plt

image = cv2.imread('gray_parrot.jpg', cv2.IMREAD_GRAYSCALE)

# Perform histogram equalization
equalized_image = cv2.equalizeHist(image)

# Plot histograms
plt.figure(figsize=(10, 5))

plt.subplot(1, 2, 1)
plt.hist(image.flatten(), 256, [0, 256], color='b')
plt.title('Original Image Histogram')


plt.subplot(1, 2, 2)
plt.hist(equalized_image.flatten(), 256, [0, 256], color='r')
plt.title('Equalized Image Histogram')

plt.show()

# Display original and equalized images
plt.figure(figsize=(10, 5))
plt.subplot(1, 2, 1)
plt.imshow(image, cmap='gray')

plt.title('Original Image')
plt.axis('off')


plt.subplot(1, 2, 2)
plt.imshow(equalized_image, cmap='gray')
plt.title('Equalized Image')
plt.axis('off')

plt.show()