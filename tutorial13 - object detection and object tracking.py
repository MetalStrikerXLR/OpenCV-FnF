# in RGB, color information cannot be extracted from luminance (intensity)

import cv2
import numpy as np


def nothing(x):
    pass

cv2.namedWindow("Tracking")
cv2.createTrackbar("LH", "Tracking", 0, 179, nothing)
cv2.createTrackbar("LS", "Tracking", 0, 255, nothing)
cv2.createTrackbar("LV", "Tracking", 0, 255, nothing)

cv2.createTrackbar("UH", "Tracking", 0, 179, nothing)
cv2.createTrackbar("US", "Tracking", 0, 255, nothing)
cv2.createTrackbar("UV", "Tracking", 0, 255, nothing)

while True:
    frame = cv2.imread('sample_images/smarties.png')
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    l_B = np.array([cv2.getTrackbarPos("LH", "Tracking"), cv2.getTrackbarPos("LS", "Tracking"), cv2.getTrackbarPos("LV", "Tracking")])    # lower color to detect
    u_B = np.array([cv2.getTrackbarPos("UH", "Tracking"), cv2.getTrackbarPos("US", "Tracking"), cv2.getTrackbarPos("UV", "Tracking")])  # upper color to detect

    mask = cv2.inRange(hsv, l_B, u_B)
    res = cv2.bitwise_and(frame, frame, mask=mask)

    cv2.imshow("frame", frame)
    cv2.imshow("hsv", hsv)
    cv2.imshow("mask", mask)
    cv2.imshow("res", res)

    key = cv2.waitKey(1)
    if key == 27:
        break

cap.release()
cv2.destroyAllWindows()