import cv2 as cv
import numpy as np

# Read the original image
img = cv.imread('input_imgs/parrot.jpg')

# Convert the image to grayscale
grayScale_img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

# Display the original and grayscale images
cv.imshow("Original Parrot", img)
cv.imshow("Grayscale Parrot", grayScale_img)

# Wait for a key event and then close the windows
cv.waitKey(0)
cv.destroyWindow("Original Parrot")
cv.destroyWindow("Grayscale Parrot")

# Create a negative image by subtracting pixel values from 255
neg_img = 255 - img

# Display the original and negative images
cv.imshow("Original Parrot", img)
cv.imshow("Negative Parrot", neg_img)

# Wait for a key event and then close the windows
cv.waitKey(0)
cv.destroyWindow("Original Parrot")
cv.destroyWindow("Negative Parrot")

# Apply thresholding to the grayscale image
thresholdVal = 127
ret, threshold_img = cv.threshold(grayScale_img, thresholdVal, 255, cv.THRESH_BINARY)
ret, threshold_img_inv = cv.threshold(grayScale_img, thresholdVal, 255, cv.THRESH_BINARY_INV)

# Display the grayscale, threshold, and inverted threshold images
cv.imshow("Grayscale Parrot", grayScale_img)
cv.imshow("Threshold Parrot", threshold_img)
cv.imshow("Threshold-inverse Parrot", threshold_img_inv)

# Wait for a key event and then close the windows
cv.waitKey(0)
cv.destroyWindow("Grayscale Parrot")
cv.destroyWindow("Threshold Parrot")
cv.destroyWindow("Threshold-inverse Parrot")

# Adjust the brightness and darkness of the grayscale image
brightness_change = 50
bright_img = np.clip(grayScale_img + brightness_change, 0, 255)
dark_img = np.clip(grayScale_img - brightness_change, 0, 255)

# Display the grayscale, brightened, and darkened images
cv.imshow("Grayscale Parrot", grayScale_img)
cv.imshow("Brightened Parrot", bright_img.astype(np.uint8))
cv.imshow("Darkened Parrot", dark_img.astype(np.uint8))

# Wait for a key event and then close the windows
cv.waitKey(0)
cv.destroyWindow("Grayscale Parrot")
cv.destroyWindow("Brightened Parrot")
cv.destroyWindow("Darkened Parrot")

# Save the grayscale and processed images to the output_imgs folder
cv.imwrite('output_imgs/gray_parrot.jpg', grayScale_img)
cv.imwrite('output_imgs/negative_parrot.jpg', neg_img)
cv.imwrite('output_imgs/threshold_parrot.jpg', threshold_img)
cv.imwrite('output_imgs/threshold-inv_parrot.jpg', threshold_img_inv)
cv.imwrite('output_imgs/bright_parrot.jpg', bright_img.astype(np.uint8))
cv.imwrite('output_imgs/dark_parrot.jpg', dark_img.astype(np.uint8))
