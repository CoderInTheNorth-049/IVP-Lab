import cv2
import numpy as np
import matplotlib.pyplot as plt

image = cv2.imread('gray_parrot.jpg', cv2.IMREAD_GRAYSCALE)

# Apply Sobel operator
sobel_x = cv2.Sobel(image, cv2.CV_64F, 1, 0, ksize=3)
sobel_y = cv2.Sobel(image, cv2.CV_64F, 0, 1, ksize=3)
sobel = np.sqrt(sobel_x**2 + sobel_y**2)

# Apply Prewitt operator
prewitt_x = cv2.filter2D(image, -1, np.array([[-1, 0, 1], [-1, 0, 1], [-1, 0, 1]]))
prewitt_y = cv2.filter2D(image, -1, np.array([[-1, -1, -1], [0, 0, 0], [1, 1, 1]]))
prewitt = np.sqrt(prewitt_x**2 + prewitt_y**2)


# Apply Roberts operator
roberts_x = cv2.filter2D(image, -1, np.array([[1, 0], [0, -1]]))
roberts_y = cv2.filter2D(image, -1, np.array([[0, 1], [-1, 0]]))
roberts = np.sqrt(roberts_x**2 + roberts_y**2)

# Plotting the results
plt.figure(figsize=(12, 8))

plt.subplot(2, 2, 1)
plt.imshow(image, cmap='gray')
plt.title('Original Image')
plt.axis('off')


plt.subplot(2, 2, 2)
plt.imshow(sobel, cmap='gray')
plt.title('Sobel Edge Detection')
plt.axis('off')


plt.subplot(2, 2, 3)
plt.imshow(prewitt, cmap='gray')
plt.title('Prewitt Edge Detection')
plt.axis('off')


plt.subplot(2, 2, 4)
plt.imshow(roberts, cmap='gray')
plt.title('Roberts Edge Detection')
plt.axis('off')
plt.show()

