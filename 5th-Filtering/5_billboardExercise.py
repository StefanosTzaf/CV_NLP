'''
4 Left clicks to get the 4 points of the billboard starting from the top left corner
and continuing anticlockwise. WARNING : If not clicked 4 times before enter it will crash
'''

import numpy as np
import cv2

def onClick(event, x, y, flags, params):
    if event == cv2.EVENT_LBUTTONDBLCLK:
        # for computing homography we need 4 points
        if len(dstPoints) < 4:
            dstPoints.append([x,y])
            # red and filled(-1 parameter)
            cv2.circle(imgCopy, (x, y), 50, (0, 0, 255), -1)
            cv2.imshow('Click', imgCopy)


baseImg = cv2.imread('../photos/billboard.jpg')
img2 = cv2.imread('../photos/ezio.jpg')

# because i will draw on the image red points where i click so i dont want it to store it in the first one
imgCopy = baseImg.copy()


# store the images height and width
baseH, baseW = baseImg.shape[:2]
img2H, img2W = img2.shape[:2]

# destination and source are flipped (destination is the base image)
srcPoints = np.float32(
    [
        #anticlockwise order
        [0,0],
        [0, img2H],
        [img2W, img2H],
        [img2W, 0],
    ]
)

dstPoints = []

cv2.namedWindow('Click', cv2.WINDOW_NORMAL)
# the name should be the same of the window we are going to click on
cv2.setMouseCallback('Click', onClick)

# show the image to be clicked
cv2.imshow('Click', baseImg)
cv2.waitKey(0)


dstFloat = np.float32(dstPoints)
# homography matrix
H = cv2.getPerspectiveTransform(srcPoints, dstFloat)

#apply the transformation to the image we want to be over the billboard
warped = cv2.warpPerspective(img2, H, (baseW, baseH) )


#create a mask for droppping the black pixels from the warped img

mask = np.zeros(baseImg.shape, dtype=np.uint8)
cv2.fillConvexPoly(mask, np.int32(dstFloat), (255, 255, 255))

cv2.namedWindow('Mask', cv2.WINDOW_NORMAL)
cv2.imshow('Mask', mask)
cv2.waitKey(0)