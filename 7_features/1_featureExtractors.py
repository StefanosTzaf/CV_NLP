import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread('../photos/lena.png')
# feature extractor
# sift - surf - orb - akaze

sift = cv2.SIFT_create()
# has a specific number of points to be extracted, we can specify it through parameter
orb = cv2.ORB_create(30)
# binary descriptor as ORB
akaze = cv2.AKAZE_create()

current = akaze

# detect keypoints and compute descriptors
# cyrcles tell us after how many gaussian piramide blurs wi will lose this feature
# the bigger the circle the more important the feature 


keypoints, descriptors = current.detectAndCompute(img, None)
cv2.drawKeypoints(img, keypoints, img, (255, 0, 0), cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)

cv2.imshow('SIFT Keypoints', img)
cv2.waitKey(0)