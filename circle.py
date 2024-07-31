gray = cv2.cvtColor(roi, cv2.COLOR_BGR2GRAY)

                # Apply Gaussian Blur to reduce noise
                blur = cv2.medianBlur(gray, 5)

                # Apply Hough's circle detection
                circles = cv2.HoughCircles(blur, cv2.HOUGH_GRADIENT_ALT, 1.5, 500,
                                        param1=100, param2=0.5,
                                        minRadius=50, maxRadius=1000)
                if circles is not None:
                    print("circle found")
                    circles = np.uint16(np.around(circles))
                    for i in circles[0, :]:
                        # draw the outer circle
                        cv2.circle(blur, (i[0], i[1]), i[2], (0, 255, 0), 2)
                        # draw the center of the circle
                        cv2.circle(blur, (i[0], i[1]), 2, (0, 0, 255), 3)