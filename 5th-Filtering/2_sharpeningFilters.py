import numpy as np
import cv2

# sharpening filters adding details!

# first approach
img = cv2.imread('../photos/lena.png')
cv2.imshow('Initial', img)
cv2.waitKey(0)


blurredImg = cv2.GaussianBlur(img, (9,9), 10)

# how significant are two pictures each for the final (1.5 means 150% in the first so we strengthen)
final = cv2.addWeighted(img, 1.5, blurredImg, -0.5, 0)
cv2.imshow('Result', final)
cv2.waitKey(0)

#second aproach
sharpenKernel = np.array(
    [
        [0,-1, 0],
        [-1,5, -1],
        [0,-1, 0]
    ]
)

final = cv2.filter2D(img, -1, sharpenKernel)
cv2.imshow('Result2', final)
cv2.waitKey(0)
