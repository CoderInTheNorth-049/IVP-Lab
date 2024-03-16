import cv2
import numpy as np
import os

# Read the input image
image = cv2.imread('input_imgs/cameraman.png')

# Ensure the image is not None
if image is not None:

    # Create the output directory if it doesn't exist
    output_dir = 'output_imgs'
    os.makedirs(output_dir, exist_ok=True)

    # Apply the average filter with a kernel size of 5x5
    average_filter = cv2.blur(image, (5, 5))
    median_filter = cv2.medianBlur(image, 5)
    gaussian_image = cv2.GaussianBlur(image, (5, 5), 0)

    # Apply Laplacian filter
    laplacian = cv2.Laplacian(image, cv2.CV_64F)

    # Convert the result to uint8 and normalize
    laplacian = cv2.convertScaleAbs(laplacian)

    kernel = np.array([[-1, -1, -1],
                       [-1, 8, -1],
                       [-1, -1, -1]])

    # Apply the high boost filter
    high_boost_image = cv2.filter2D(image, -1, kernel)

    # Save the filtered images
    cv2.imwrite(os.path.join(output_dir, 'average_filter.jpg'), average_filter)
    cv2.imwrite(os.path.join(output_dir, 'median_filter.jpg'), median_filter)
    cv2.imwrite(os.path.join(output_dir, 'gaussian_image.jpg'), gaussian_image)
    cv2.imwrite(os.path.join(output_dir, 'laplacian_image.jpg'), laplacian)
    cv2.imwrite(os.path.join(output_dir, 'high_boost_image.jpg'), high_boost_image)

    # Display the original and filtered images
    cv2.imshow('Original Image', image)
    cv2.imshow('Average_filter', average_filter)
    cv2.imshow('Median_filter', median_filter)
    cv2.imshow('Gaussian_image', gaussian_image)
    cv2.imshow('Laplacian_image', laplacian)
    cv2.imshow('High Boost Filtered Image', high_boost_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

else:
    print("Error loading the image.")
