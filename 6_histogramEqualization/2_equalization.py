'''Histogram equalization is a technique used in image processing to enhance
contrast by redistributing pixel intensity values.
It works by transforming the image's histogram so that the intensities
are more evenly spread across the full range 
[0,255] in an 8-bit image.
'''

import cv2
import numpy as np
import matplotlib.pyplot as plt


img = cv2.imread("../photos/lena.png", 0)

img_eq = cv2.equalizeHist(img)

cv2.imshow('EQ', np.hstack((img, img_eq)))
cv2.waitKey(0)


# Equalization effect on Color Image
img = cv2.imread("../photos/lena.png")
eq_channels =  []
channels = cv2.split(img)

for ch in channels:
  eq_channels.append(cv2.equalizeHist(ch))

img_eq = cv2.merge(eq_channels)
cv2.imshow('Colourful', np.hstack((img,img_eq)))
cv2.waitKey(0)
cv2.destroyAllWindows()