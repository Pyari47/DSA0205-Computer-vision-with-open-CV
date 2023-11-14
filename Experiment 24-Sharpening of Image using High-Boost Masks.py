import cv2
import numpy as np

# Load the image
image = cv2.imread("C:/Users/LENOVO/OneDrive/Desktop/CV pic/image 1.jpg")

# Convert the image to grayscale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Apply a Gaussian blur to create a low-pass filtered version of the image
blurred = cv2.GaussianBlur(gray, (5, 5), 0)

# Calculate the high-boost mask by subtracting the low-pass filtered image from the original image
high_boost_mask = gray - blurred

# You can adjust the boost factor to control the sharpening effect
boost_factor = 1.5
sharpened = gray + boost_factor * high_boost_mask

# Clip the values to ensure they are within the 0-255 range
sharpened = np.clip(sharpened, 0, 255).astype(np.uint8)

# Display the original and sharpened images
cv2.imshow('Original Image', gray)
cv2.imshow('Sharpened Image', sharpened)

cv2.waitKey(0)
cv2.destroyAllWindows()
