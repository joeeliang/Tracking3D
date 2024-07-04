import cv2
import numpy as np

# Initialize the camera
cap = cv2.VideoCapture(0)

# Define the color range for the object to track (e.g., blue color)
lower_purple = np.array([125, 50, 50])
upper_purple = np.array([150, 255, 255])
while True:
    # Capture frame-by-frame
    ret, frame = cap.read()
    
    if not ret:
        break
    
    # Convert the frame to HSV color space
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    
    # Create a mask for the color
    mask = cv2.inRange(hsv, lower_purple, upper_purple)
    
    # Find contours
    contours, _ = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    
    if contours:
        # Find the largest contour
        largest_contour = max(contours, key=cv2.contourArea)
        
        # Get the bounding box coordinates
        x, y, w, h = cv2.boundingRect(largest_contour)
        
        # Calculate the center of the bounding box
        center_x = x + w // 2
        center_y = y + h // 2
        
        # Draw the bounding box and center point on the frame
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
        cv2.circle(frame, (center_x, center_y), 5, (0, 255, 0), -1)
        
        # Display the coordinates
        cv2.putText(frame, f"X: {center_x}, Y: {center_y}", (center_x - 50, center_y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2)
        
        # Print the coordinates
        print(f"Object coordinates: X: {center_x}, Y: {center_y}")
    
    # Display the resulting frame
    cv2.imshow('Frame', frame)
    cv2.imshow('Mask', mask)
    
    # Break the loop on 'q' key press
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the camera and close all OpenCV windows
cap.release()
cv2.destroyAllWindows()
