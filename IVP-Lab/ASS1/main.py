import cv2 as cv

# Read the original image
img = cv.imread('input_imgs/parrot.jpg')

# Convert the image to grayscale
grayScale_img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

# Display the original and grayscale images
cv.imshow("parrot", img)
cv.imshow("grayscale parrot", grayScale_img)

# Wait for a key event and then close the windows
cv.waitKey(0)
cv.destroyAllWindows()

# Save the grayscale image to the output_imgs folder
cv.imwrite('output_imgs/gray_parrot.jpg', grayScale_img)
