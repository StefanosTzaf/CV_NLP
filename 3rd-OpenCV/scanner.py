'''
Program that acts like document scanner
'''
# for now we found the corners my clicking with the mouse manually and not automatically(laeter)

import cv2
import numpy as np

img = cv2.imread('../photos/gerry.png')

#define the starting points - the corners of the original image(manually - not a good way)
tl = [28,227]
bl = [131,987]
br = [730,860]
tr = [572,149]

srcPoints = np.array(
    [
        [tl],
        [bl],
        [br],
        [tr]
    ], np.float32
)

#define the destination points i.e. the corners of the resolution of the final image e.g. 800x600
#needing 3 points in affine transformation only in perspective - homography needing 4
dstPoints = np.array(
    [
        [0,0],
        [0,800],
        [600,800],
        [600,0]
    ], np.float32
)

# get the transformation matrix M
M = cv2.getPerspectiveTransform(srcPoints, dstPoints)

outImage = cv2.warpPerspective(img, M, (600,800))

cv2.imshow('Original', img)
cv2.waitKey(0)

cv2.imshow('New', outImage)  
cv2.waitKey(0)