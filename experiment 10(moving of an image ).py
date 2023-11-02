import cv2
import numpy as np

# Load the image you want to move
image = cv2.imread("C:/Users/thanv/OneDrive/Desktop/cv pics/image 3.jpeg")

# Create a blank canvas (background)
canvas = np.zeros((500, 500, 3), dtype=np.uint8)  # Create a black canvas of size 500x500

# Define the coordinates where you want to move the image
x_offset, y_offset = 100, 100  # Change these values to move the image to a different location

# Copy the image to the specified coordinates on the canvas
canvas[y_offset:y_offset + image.shape[0], x_offset:x_offset + image.shape[1]] = image

# Display or save the canvas with the moved image
cv2.imshow("Moved Image", canvas)
cv2.waitKey(0)
cv2.destroyAllWindows()

