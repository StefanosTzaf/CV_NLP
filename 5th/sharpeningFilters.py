#sharpening filters adding details!

import numpy as np
import cv2

#averaging filters are the blurred filters(blured algorithms are used to reduce the noise)
#salt and pepper noise is like in this photo
img = cv2.imread('../photos/lena.png')
cv2.imshow('Initial', img)
cv2.waitKey(0)

filteredImg = cv2.GaussianBlur(img, (9,9), 10)

cv2.imshow('Filter', filteredImg)
cv2.waitKey(0)

#how significant are two pictures each for the final
final = cv2.addWeighted(img,1.5,filteredImg, -0.5,0)

#second aproach

sharpenKernel = np.array([
    [0,-1,0],
    [-1,5,-1],
    [0,-1,0]
])

final = cv2.filter2D(img, -1, sharpenKernel)


cv2.imshow('Result', final)
cv2.waitKey(0)