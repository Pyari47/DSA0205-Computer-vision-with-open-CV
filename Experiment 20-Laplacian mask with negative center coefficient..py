import cv2
import numpy as np

img = cv2.imread("C:/Users/LENOVO/OneDrive/Desktop/CV pic/image 2.webp")
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
kernel = np.array([[0, 1, 0], [1, -8, 1], [0, 1, 0]])
sharpened = cv2.filter2D(gray, -1, kernel)

# Enhance the contrast for a more visible sharpness effect
sharpened = cv2.convertScaleAbs(sharpened, alpha=2.0, beta=0)

# Enhance the edges using the Laplacian filter
edges = cv2.Laplacian(sharpened, cv2.CV_16S)
edges = cv2.convertScaleAbs(edges)

cv2.imshow('Original', gray)
cv2.imshow('Sharpened', sharpened)
cv2.imshow('Enhanced Edges', edges)
cv2.waitKey(0)
cv2.destroyAllWindows()
