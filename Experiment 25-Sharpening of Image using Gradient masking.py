import cv2
import numpy as np

# Load the image
image = cv2.imread("C:/Users/LENOVO/OneDrive/Desktop/CV pic/image 3.jpg")

# Convert the image to grayscale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Apply Sobel filters to calculate gradients in both the x and y directions
gradient_x = cv2.Sobel(gray, cv2.CV_64F, 1, 0, ksize=3)
gradient_y = cv2.Sobel(gray, cv2.CV_64F, 0, 1, ksize=3)

# Combine the gradient images to get the gradient magnitude
gradient_magnitude = cv2.magnitude(gradient_x, gradient_y)

# Normalize the gradient magnitude to the 0-255 range
gradient_magnitude = cv2.normalize(gradient_magnitude, None, 0, 255, cv2.NORM_MINMAX)

# You can adjust the boost factor to control the sharpening effect
boost_factor = 1.5

# Convert the gradient_magnitude to the same data type as gray
gradient_magnitude = gradient_magnitude.astype(gray.dtype)

# Apply the sharpening using cv2.addWeighted
sharpened = cv2.addWeighted(gray, 1 + boost_factor, gradient_magnitude, -boost_factor, 0)

# Display the original and sharpened images
cv2.imshow('Original Image', gray)
cv2.imshow('Sharpened Image', sharpened)

cv2.waitKey(0)
cv2.destroyAllWindows()

