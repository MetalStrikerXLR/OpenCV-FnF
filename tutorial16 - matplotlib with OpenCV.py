import matplotlib.pyplot as plot # it is in RGB unlike openCV which is in BGR
import numpy as np
import cv2

img = cv2.imread('sample_images/gradient.png', 0)

ret, th1 = cv2.threshold(img, 50, 255, cv2.THRESH_BINARY)
ret1, th2 = cv2.threshold(img, 200, 255, cv2.THRESH_BINARY_INV)
ret2, th3 = cv2.threshold(img, 100, 255, cv2.THRESH_TRUNC)   # Cutoff
ret3, th4 = cv2.threshold(img, 127, 255, cv2.THRESH_TOZERO)  # Less than threshold is zero
ret4, th5 = cv2.threshold(img, 127, 255, cv2.THRESH_TOZERO_INV)

titles = ['Original', 'Binary', 'Inv Binary', 'Trunc', 'ToZero', 'Inv ToZero']
images = [img, th1, th2, th3, th4, th5]

for i in range(6):
    plot.subplot(2, 3, i+1)
    plot.imshow(images[i], 'gray')
    plot.title(titles[i])

    plot.xticks([])
    plot.yticks([])

plot.show()