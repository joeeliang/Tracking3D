import cv2
import numpy as np
import cameraTrack
import matplotlib.pyplot as plt

# Initialize the cameras
cap1 = cv2.VideoCapture(0)  # First camera
cap2 = cv2.VideoCapture(1)  # Second camera

#width = 1280
#height = 720
#cap1.set(cv2.CAP_PROP_FRAME_WIDTH, width)
#cap1.set(cv2.CAP_PROP_FRAME_HEIGHT, height)
#cap2.set(cv2.CAP_PROP_FRAME_WIDTH, width)
#cap2.set(cv2.CAP_PROP_FRAME_HEIGHT, height)

# Define the color range for the object to track (e.g., purple color)
# These values might need adjustment depending on the specific shade of purple and lighting conditions
lower = np.array([130, 50, 50])
upper = np.array([255, 255, 255])

def process_frame(frame):
    # Convert the frame to HSV color space
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    
    # Create a mask for the color
    mask = cv2.inRange(hsv, lower, upper)
    
    # Find contours
    contours, _ = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    center_x = None
    center_y = None
    
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
    
    return frame, mask, center_x, center_y

def generate_data_stream():
    while True:
        x = np.random.rand()
        y = np.random.rand()
        yield (x, y)

data_stream = generate_data_stream()

# Initialize the plot
plt.ion()  # Turn on interactive mode
fig, ax = plt.subplots()
scatter = ax.scatter([], [], c='b')  # 'b' stands for blue color
ax.set_xlim(0, 55)
ax.set_ylim(0, 55)

# Function to update the plot
def update_plot(x):
    scatter.set_offsets(np.array([[x[0], x[1]]]))
    plt.draw()  # Update plot


while True:
    # Capture frame-by-frame from both cameras
    ret1, frame1 = cap1.read()
    ret2, frame2 = cap2.read()
    
    if not ret1:
        break
    
    # Process frames
    processed_frame1, mask1, p1, p1y = process_frame(frame1)
    processed_frame2, mask2, p2, p2y= process_frame(frame2)

    if p1 is not None and p2 is not None:
        update_plot(cameraTrack.triangulate_XY(p1, p2))
        # plt.show()
    if p1y is not None and p2y is not None:
        print("z: " + str(cameraTrack.triangulate_Z(p1y, p2y)))
    
    # Display the resulting frames
    cv2.imshow('Frame 1', processed_frame1)
    cv2.imshow('Mask 1', mask1)
    cv2.imshow('Frame 2', processed_frame2)
    cv2.imshow('Mask 2', mask2)
    
    # Break the loop on 'q' key press
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the cameras and close all OpenCV windows
cap1.release()
cap2.release()
cv2.destroyAllWindows()