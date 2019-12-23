import cv2
import numpy as np

# img = cv2.imread('sample_images/lena.jpg', 1)
img = np.zeros([512, 512, 3], np.uint8)

img = cv2.line(img, (0, 0), (255, 255), (147, 96, 44), 10)
img = cv2.arrowedLine(img, (0, 255), (255, 255), (0, 96, 44), 10)

img = cv2.rectangle(img, (384, 0), (510, 128), (16, 0, 44), 8)
img = cv2.circle(img, (447, 63), 63, (0, 255, 255), -1)

font = cv2.FONT_HERSHEY_COMPLEX
img = cv2.putText(img, 'OpenCV', (10, 500), font, 4, (0, 255, 255), 10, cv2.LINE_AA)

cv2.imshow('Image', img)

cv2.waitKey(0)
cv2.destroyAllWindows()