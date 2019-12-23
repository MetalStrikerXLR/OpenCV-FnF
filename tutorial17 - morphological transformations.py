import cv2
import numpy as np
from matplotlib import pyplot as plot

img = cv2.imread('sample_images/smarties.png', cv2.IMREAD_GRAYSCALE)

ret, mask = cv2.threshold(img, 220, 255, cv2.THRESH_BINARY_INV)

kernal = np.ones((2, 2), np.uint8)
dilation = cv2.dilate(mask, kernal, iterations=2)
erosion = cv2.erode(mask, kernal, iterations=2)
opening = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernal, iterations=1)  # erosion then dilation
closing = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernal, iterations=1)  # dilation then erosion
mg = cv2.morphologyEx(mask, cv2.MORPH_GRADIENT, kernal, iterations=1)
th = cv2.morphologyEx(mask, cv2.MORPH_TOPHAT, kernal, iterations=1)

titles = ['image', 'mask', 'dilation', 'erosion', 'open', 'close', 'gradient', 'tophat']
images =[img, mask, dilation, erosion, opening, closing, mg, th]

for i in range(8):
    plot.subplot(2, 4, i+1)
    plot.imshow(images[i], 'gray')
    plot.title(titles[i])
    plot.xticks([])
    plot.yticks([])


plot.show()