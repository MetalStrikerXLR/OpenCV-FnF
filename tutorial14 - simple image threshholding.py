# Thresholding = removing background

import cv2
import numpy as np

img = cv2.imread('sample_images/gradient.png', 0)

ret, th1 = cv2.threshold(img, 50, 255, cv2.THRESH_BINARY)
ret1, th2 = cv2.threshold(img, 200, 255, cv2.THRESH_BINARY_INV)
ret2, th3 = cv2.threshold(img, 100, 255, cv2.THRESH_TRUNC)   # Cutoff
ret3, th4 = cv2.threshold(img, 127, 255, cv2.THRESH_TOZERO)  # Less than threshold is zero
ret4, th5 = cv2.threshold(img, 127, 255, cv2.THRESH_TOZERO_INV)

cv2.imshow("Image", img)
cv2.imshow("Binary Threshold Image", th1)
cv2.imshow("INV Binary Threshold Image", th2)
cv2.imshow("TRUNC Threshold Image", th3)
cv2.imshow("ToZero Threshold Image", th4)
cv2.imshow("INV ToZero Threshold Image", th5)

cv2.waitKey(0)
cv2.destroyAllWindows()