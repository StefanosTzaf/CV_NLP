import cv2
import numpy as np
import matplotlib.pyplot as plt


img = cv2.imread("../photos/lena.png")

# change color space to HSV
hsv_img = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
# hue : color, saturation : color intensity, value : color brightness
h,s,v = cv2.split(hsv_img)


# equalize the value channel only
eq_v = cv2.equalizeHist(v)
img_eq = cv2.merge((h,s,eq_v))

# go back to BGR color space
img_eq = cv2.cvtColor(img_eq, cv2.COLOR_HSV2BGR) # imshow uses BGR

cv2.imshow('Photos',np.hstack((img,img_eq)))
cv2.waitKey(0)