'''script that loads two pictures and with
the automatic features extraction stiches them together'''

import cv2
import numpy as np

img1 = cv2.imread('../photos/right.png')
img2 = cv2.imread('../photos/left.png')

# create feature extractor
orb = cv2.ORB_create()

# compute the features

# keypoints are the points of interest in the image
# The descriptor is a numerical representation that 
# summarizes the information around a keypoint in an image.
# In other words, after the algorithm detects a keypoint, the descriptor
# generates a vector (often binary for algorithms like ORB) that describes
# the local features—such as textures, patterns, and orientations—of that specific point.
keypoints1, desc1 = orb.detectAndCompute(img1,None)
keypoints2, desc2 = orb.detectAndCompute(img2,None)

# create a matcher and match the keypoints (BF = bruteforce) 
matcher = cv2.BFMatcher(cv2.NORM_HAMMING)
# knn = k nearest neighbors 
matches = matcher.knnMatch(desc1,desc2,k=2)
goodMatches = []

# apply ratio test
for m,n in matches:
    if m.distance < 0.6 * n.distance:
        goodMatches.append(m)

# check if we have at least 4 points for perspective transform

if len(goodMatches) > 4:
    # in OpenCv, the two images involved in the match are called query img and trainImg
    # so queryImg is the index of the point belonging to query img while trainIdx is the point belonging to trainImg
    srcPoints = np.float32([keypoints1[m.queryIdx].pt for m in goodMatches])
    dstPoints = np.float32([keypoints2[m.trainIdx].pt for m in goodMatches])

# use this function not the GEtperspectiveTransform because i can give more than 4 points 
M, mask = cv2.findHomography(srcPoints, dstPoints)

# transform the images to make them fit

# get rid of the black pixels to the right that exist due to the transformation with -int(M[0,2])
dst = cv2.warpPerspective(img1, M, (img1.shape[1] + img2.shape[1] - int(M[0,2]), img1.shape[0] ))

# copy the pixels of img2 inside dst, that already contrains the pixels of img1
dst[0:img2.shape[0], 0:img2.shape[1]] = img2.copy()

cv2.namedWindow('Panorama', cv2.WINDOW_NORMAL)
cv2.imshow('Panorama', dst)
cv2.waitKey(0)