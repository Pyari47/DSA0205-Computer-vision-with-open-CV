import cv2

# Open the webcam
cap = cv2.VideoCapture(0)

# Define the desired frame rate (frames per second)
desired_fps = 30  # Adjust this value to speed up or slow down

# Set the frame rate of the webcam
cap.set(cv2.CAP_PROP_FPS, desired_fps)

while True:
    ret, frame = cap.read()
    
    if not ret:
        break

    cv2.imshow("frame", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
