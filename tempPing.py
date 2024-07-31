# Temporary file to give leon data points to track parabolic trajectory of a ping pong ball.
import cv2
import numpy as np
import pickle

# Define the lower and upper bounds for the color of a basketball in HSV
lower_orange = np.array([1, 50, 50])
upper_orange = np.array([30, 225, 255])

# Open the video capture
cap = cv2.VideoCapture(0)  # Use 0 for webcam or replace with video file path

# Create and initialize the color histogram
hist = None
roi = None

def load_histogram(filename='histogram.pkl'):
    with open(filename, 'rb') as file:
        hist = pickle.load(file)
    print(f"Histogram loaded from {filename}")
    return hist

def bounding_box(x,y,w,h,t):
    '''This function returns the new, expanded bounding box'''
    nx = max(0, x - t)
    ny = max(0, y - t)
    max_x = min(1920, x + w + t)
    max_y = min(1080, y + h + t)

    return int(nx), int(ny), int(max_x), int(max_y)

coords = []

def start():
    hist = load_histogram()
    while True:
        ret, frame = cap.read()
        if not ret:
            break
        
        # Convert the frame to HSV color space
        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        
        # Calculate the back projection
        dst = cv2.calcBackProject([hsv], [0, 1], hist, [0, 180, 0, 256], 1)
        
        # Apply a binary threshold to eliminate low probability pixels
        _, thresh = cv2.threshold(dst, 50, 255, cv2.THRESH_BINARY)
        
        # Apply morphological operations to reduce noise
        kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (5, 5))
        thresh = cv2.morphologyEx(thresh, cv2.MORPH_OPEN, kernel)
        
        # Find contours in the thresholded image
        contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        
        # Draw contours and find the largest one (assumed to be the ball)
        max_area = 0
        max_contour = None
        for contour in contours:
            area = cv2.contourArea(contour)
            if area > max_area:
                max_area = area
                max_contour = contour
        
        if max_contour is not None:
            # Draw the largest contour
            cv2.drawContours(frame, [max_contour], 0, (0, 255, 0), 2)
            # Compute the moments of the largest contour
            M = cv2.moments(max_contour)

            # Calculate the center of the contour
            if M['m00'] != 0:
                cx = int(M['m10'] / M['m00'])
                cy = int(M['m01'] / M['m00'])
            x, y, w, h = cv2.boundingRect(max_contour)

            x, y, max_x, max_y = bounding_box(x,y,w,h, 400)

            roi = frame[y:max_y, x:max_x]  # extract ROI from original thresholded image
            cv2.rectangle(frame,(x,y),(max_x, max_y),(0, 0, 255),3)
            coords.append([cx,cy])
            # coords.append([x,y])

        # Display the original frame and the thresholded image
        cv2.imshow('Frame', frame)
        cv2.imshow('Thresholded', thresh)
        
        # Exit on pressing 'q'
        if cv2.waitKey(1) & 0xFF == ord('q'):
            np.save('center_coords.npy', coords)
            break

    # Release the capture and close the windows
    cap.release()
    cv2.destroyAllWindows()

def main():
    while True:
        ret, frame = cap.read()
        if not ret:
            break
        
        # cv2.imshow('Recording', frame)
        start()
        
        key = cv2.waitKey(1) & 0xFF
        if key == ord('q'):
            break


if __name__ == "__main__":
    main()