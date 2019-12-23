# Thresholding = removing background

import cv2
import numpy as np

img = cv2.imread('sample_images/sudoku.png', 0)

ret, th1 = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)
th2 = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 11, 2) # mean of threshold value in neighbourhood
th3 = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 2) # weighted average of threshold value in neighbourhood

cv2.imshow("Image", img)
cv2.imshow("Binary Threshold Image", th1)
cv2.imshow("Mean-C Adaptive Threshold Image", th2)
cv2.imshow("Gaussian Adaptive Threshold Image", th3)

cv2.waitKey(0)
cv2.destroyAllWindows()