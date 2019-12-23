import numpy as np
import cv2

img = cv2.imread('sample_images/opencv-logo.png')
imgGray = cv2.imread('sample_images/opencv-logo.png', cv2.IMREAD_GRAYSCALE)

ret, thresh = cv2.threshold(imgGray, 127, 255, 0)
contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)

print("Number of Contours: " + str(len(contours)))

cv2.drawContours(img, contours, 8, (0, 255, 255), 3)

cv2.imshow('Image', img)
cv2.imshow('Image Gray', imgGray)
cv2.waitKey(0)
cv2.destroyAllWindows()