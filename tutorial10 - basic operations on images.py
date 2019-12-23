import numpy as np
import cv2

img = cv2.imread('sample_images/messi5.jpg')
img2 = cv2.imread('sample_images/opencv-logo.png')

print(img.shape)  # returns tuple of number of rows, columns and channels
print(img.size)   # returns total number of pixels in image
print(img.dtype)  # return image datatype

b, g, r = cv2.split(img)
img = cv2.merge((b, g, r))

ball = img[280:340, 330:390]
img[273:333, 100:160] = ball

img = cv2.resize(img, (512, 512))
img2 = cv2.resize(img2, (512, 512))

# added_img = cv2.add(img, img2)
added_img = cv2.addWeighted(img, .6, img2, .4, 0)
cv2.imshow('image', added_img)

cv2.waitKey(0)
cv2.destroyAllWindows()