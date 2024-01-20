import cv2 as cv

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

# Save the grayscale and negative images to the output_imgs folder
cv.imwrite('output_imgs/gray_parrot.jpg', grayScale_img)
cv.imwrite('output_imgs/negative_parrot.jpg', neg_img)
