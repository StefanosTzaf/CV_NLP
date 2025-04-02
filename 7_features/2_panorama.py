'''script that loads two pictures and with
the automatic features extraction stiches them together'''

import cv2
import numpy as np

img1 = cv2.imread('../photos/right.png')
img2 = cv2.imread('../photos/left.png')

# create feature extractor
orb = cv2.ORB_create()

# compute the features

keypoints1, desc1 = orb.detectAndCOmpute(img1,None)
keypoints2, desc2 = orb.detectAndCOmpute(img2,None)

# create a matcher and match the keypoints (BF = bruteforce) 
matcher = cv2.BFMatcher(cv2.NORM_HAMMING)
# knn = k nearest neighbors 
matches = matcher.knnMatch(desc1,desc2,k=2)
