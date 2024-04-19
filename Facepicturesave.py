import cv2

# Initialize the webcam
cap = cv2.VideoCapture(0)

# Check if the webcam is opened successfully
if not cap.isOpened():
    print("Error: Unable to open webcam.")
    exit()

# Read a frame from the webcam
ret, frame = cap.read()

# Check if the frame is read successfully
if not ret:
    print("Error: Unable to read frame.")
    exit()

# Display the frame
cv2.imshow('Webcam', frame)

# Wait for a key press
print("Press 's' to save the photo or 'q' to quit.")
key = cv2.waitKey(0)

# Save the photo if 's' is pressed
if key == ord('s'):
    cv2.imwrite('photo.jpg', frame)
    print("Photo saved successfully as 'photo.jpg'.")
elif key == ord('q'):
    print("Exiting without saving.")
else:
    print("Invalid key pressed. Exiting without saving.")

# Release the webcam and close OpenCV windows
cap.release()
cv2.destroyAllWindows()
