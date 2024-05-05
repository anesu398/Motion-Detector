import cv2
import numpy as np

# Initialize video capture
cap = cv2.VideoCapture(0)

# Initialize variables
frame_width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
frame_height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
prev_frame = None

# Main loop
while True:
    # Read frame from webcam
    ret, frame = cap.read()

    # Convert frame to grayscale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    gray = cv2.GaussianBlur(gray, (21, 21), 0)

    # Store the first frame for comparison
    if prev_frame is None:
        prev_frame = gray
        continue

    # Compute absolute difference between current frame and previous frame
    delta_frame = cv2.absdiff(prev_frame, gray)
    thresh_delta = cv2.threshold(delta_frame, 30, 255, cv2.THRESH_BINARY)[1]
    thresh_delta = cv2.dilate(thresh_delta, None, iterations=2)

    # Find contours of motion
    contours, _ = cv2.findContours(thresh_delta.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # Draw bounding boxes around moving objects
    for contour in contours:
        if cv2.contourArea(contour) < 1000:  # Adjust area threshold as needed
            continue
        x, y, w, h = cv2.boundingRect(contour)
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 3)

    # Display frame with motion detection
    cv2.imshow('Motion Detector', frame)
    cv2.imshow('Threshold', thresh_delta)

    # Update previous frame
    prev_frame = gray

    # Check for key press (press 'q' to exit)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release resources
cap.release()
cv2.destroyAllWindows()
