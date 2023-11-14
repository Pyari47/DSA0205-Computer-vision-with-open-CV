import cv2
img=cv2.imread("C:/Users/LENOVO/OneDrive/Desktop/CV pic/Picture1.png")
x,y=100,100
width,height=300,250
roi=img[y:y+height,x:x+width]
cv2.imshow('ROI',roi)
cv2.waitKey(0)
cv2.destroyAllWindows()
