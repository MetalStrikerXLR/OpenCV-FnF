import numpy as np
import cv2

img1 = np.zeros((250, 500, 3), np.uint8)
img1 = cv2.rectangle(img1, (200, 0), (300, 100), (255, 255, 255), -1)
img2 = cv2.imread('sample_images/gradient.png')
img2 = cv2.resize(img2, (500, 250))

bitAND = cv2.bitwise_and(img2, img1)
bitOR = cv2.bitwise_or(img2, img1)
bitXOR = cv2.bitwise_xor(img2, img1)
bitNOT = cv2.bitwise_not(img2, img1)

cv2.imshow("image 1", img1)
cv2.imshow("image 2", img2)
cv2.imshow("AND", bitAND)
cv2.imshow("OR", bitOR)
cv2.imshow("XOR", bitXOR)
cv2.imshow("NOT", bitNOT)

cv2.waitKey(0)
cv2.destroyAllWindows()