import cv2

cap = cv2.VideoCapture("C:/Users/thanv/Downloads/video_of_race_car_passing_by (1080p).mp4")

if not cap.isOpened():
    print("Error opening video file")

speed = 1  # Default speed (normal)
while cap.isOpened():
    ret, frame = cap.read()

    if ret:
        cv2.imshow('Frame', frame)
        
        # Check for user input to adjust speed
        key = cv2.waitKey(1)
        if key == ord('q'):
            break
        elif key == ord('+'):
            speed += 1
        elif key == ord('-'):
            if speed > 1:
                speed -= 1

        if speed <= 0:
            speed = 1

        # Adjust waiting time based on speed
        adjusted_wait_time = int(1 / speed)
        if cv2.waitKey(adjusted_wait_time) & 0xFF == ord('q'):
            break
    else:
        break

cap.release()
cv2.destroyAllWindows()
