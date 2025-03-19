import numpy as np
import cv2

img = cv2.imread('../photos/lena.png')

# create binary mask (shape so as to have the images the same size)
mask = np.zeros(img.shape, dtype = np.uint8)
mask = cv2.rectangle(mask, (100, 100), (250, 250), (255, 255, 255), -1)

# apply the mask to the image

# and operation : if BOTH the pixels are different from 0 the higher will be in the output otherwise 0(black)
andImg = cv2.bitwise_and(img, mask)

# or operation : if one or 2 pixels are different from 0 the higher will be in the output otherwise if 1 is zero the other is shown
orImg = cv2.bitwise_or(img, mask)

# xor operation : xor in every pixel (so if one at least is black the other will be shown)
xor = cv2.bitwise_xor(img, mask)

# not operation : if the pixel is 0 it will be 255 and the oposite. In other colors just takes the binary number of the colours and inverts it
notImg = cv2.bitwise_not(img)


cv2.imshow('Mask', mask)
cv2.waitKey(0)
cv2.imshow('And', andImg)
cv2.waitKey(0)
cv2.imshow('Or', orImg)
cv2.waitKey(0)
cv2.imshow('Xor', xor)
cv2.waitKey(0)
cv2.imshow('Not', notImg)
cv2.waitKey(0)
