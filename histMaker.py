import cv2
import numpy as np
import pickle

# Open the video capture
cap = cv2.VideoCapture(0)  # Use 0 for webcam or replace with video file path

# Create and initialize the color histogram
hist = None

def selection(frame):
    roi = cv2.selectROI("Select Ball", frame, False, False)
    roi_hist = frame[int(roi[1]):int(roi[1]+roi[3]), int(roi[0]):int(roi[0]+roi[2])]
    return roi_hist

def create_histogram(roi):
    lower_orange = np.array([3,100,100])
    upper_orange = np.array([25, 255, 255])
    # Select a region of interest (ROI) containing the ball
    
    # Convert ROI to HSV color space
    hsv_roi = cv2.cvtColor(roi, cv2.COLOR_BGR2HSV)
    
    # Create a mask for the color of the basketball in the ROI
    mask = cv2.inRange(hsv_roi, lower_orange, upper_orange)
    
    # Calculate the color histogram
    hist = cv2.calcHist([hsv_roi], [0, 1], mask, [180, 256], [0, 180, 0, 256])
    
    # Normalize the histogram
    cv2.normalize(hist, hist, 0, 255, cv2.NORM_MINMAX)
    print(hist)
    save_histogram(hist)
    return hist

def save_histogram(hist, filename='orange.pkl'):
    with open(filename, 'wb') as file:
        pickle.dump(hist, file)
    print(f"Histogram saved to {filename}")


if __name__ == "__main__":
    while True:
        ret, frame = cap.read()
        if not ret:
            break
        cv2.imshow('Recording', frame)
        
        key = cv2.waitKey(1) & 0xFF
        if key == ord('q'):
            roi = selection(frame)
            create_histogram(roi)
            break