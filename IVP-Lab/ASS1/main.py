import cv2 as cv
import numpy as np

# Read the original image
img = cv.imread('input_imgs/parrot.jpg')

# Convert the image to grayscale
grayScale_img = cv.cvtColor(img, cv.COLOR_RGB2GRAY)

# Display the original and grayscale images
cv.imshow("Original Parrot", img)
cv.imshow("Grayscale Parrot", grayScale_img)

# Wait for a key event and then close the windows
cv.waitKey(0)
cv.destroyAllWindows()

# Create a negative image by subtracting pixel values from 255
neg_img = 255 - img

# Display the original and negative images
cv.imshow("Original Parrot", img)
cv.imshow("Negative Parrot", neg_img)

# Wait for a key event and then close the windows
cv.waitKey(0)
cv.destroyAllWindows()

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
cv.destroyAllWindows()

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
cv.destroyAllWindows()

# Bit-plane manipulation
h, w = grayScale_img.shape
bit_planes = np.zeros((8, h, w), dtype=np.uint8)

for bit_pos in range(8):
    bit_planes[bit_pos] = (grayScale_img >> bit_pos) & 1
    bit_planes[bit_pos] *= 255
    cv.imshow(f'Bit Plane {bit_pos}', bit_planes[bit_pos])
    cv.imwrite(f'output_imgs/bit_plane_{bit_pos}.jpg', bit_planes[bit_pos])

# Wait for a key event and then close the windows
cv.waitKey(0)
cv.destroyAllWindows()

# Save the grayscale and processed images to the output_imgs folder
cv.imwrite('output_imgs/gray_parrot.jpg', grayScale_img)
cv.imwrite('output_imgs/negative_parrot.jpg', neg_img)
cv.imwrite('output_imgs/threshold_parrot.jpg', threshold_img)
cv.imwrite('output_imgs/threshold-inv_parrot.jpg', threshold_img_inv)
cv.imwrite('output_imgs/bright_parrot.jpg', bright_img.astype(np.uint8))
cv.imwrite('output_imgs/dark_parrot.jpg', dark_img.astype(np.uint8))
