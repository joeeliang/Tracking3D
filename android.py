import cv2

def list_and_show_webcams(max_cameras=10):
    """
    List and show all connected webcams.
    
    Args:
    max_cameras (int): The maximum number of camera indices to check. Default is 10.
    """
    active_cameras = []
    
    for cam_index in range(max_cameras):
        cap = cv2.VideoCapture(cam_index)
        if cap.isOpened():
            print(f"Camera {cam_index} is active.")
            active_cameras.append(cam_index)
            ret, frame = cap.read()
            if ret:
                cv2.imshow(f'Camera {cam_index}', frame)
            cap.release()
        else:
            print(f"Camera {cam_index} is not active.")
    
    if not active_cameras:
        print("No active cameras found.")
    else:
        print(f"Active cameras: {active_cameras}")
    
    # Wait until any key is pressed to close the windows
    cv2.waitKey(0)
    cv2.destroyAllWindows()

# # Open the default camera (camera 0)
# cap = cv2.VideoCapture(0)
# cap1 = cv2.VideoCapture(1)

# while True:
#     # Read a frame from the camera
#     ret, frame = cap.read()
#     ret1, frame1 = cap1.read()
    
#     # If the frame was read successfully, display it
#     if ret:
#         cv2.imshow('Camera 0', frame)

#     if ret1:
#         cv2.imshow('Camera 1', frame1)
    
#     # Exit on key press
#     if cv2.waitKey(1) & 0xFF == ord('q'):
#         break

# # Release the camera and close the window
# cap.release()
# cap1.release()
# cv2.destroyAllWindows()

if __name__ == "__main__":
    list_and_show_webcams(max_cameras=10)
