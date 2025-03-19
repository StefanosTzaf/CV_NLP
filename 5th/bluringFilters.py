import numpy as np
import cv2

#random kernel of my own
myKernel = np.array([
    [1, 0, 1],
    [1, 0, 1],
    [1, 0, 1]
]) 

#averaging filters are the blurred filters(blured algorithms are used to reduce the noise)
#salt and pepper noise is like in this photo
img = cv2.imread('../photos/salt_pepper.png')
cv2.imshow('Initial', img)
cv2.waitKey(0)

#with a very big matrix for bluring a keep just the colors not the details
filteredImg = cv2.filter2D(img, -1, myKernel)

filteredImg = cv2.blur(img , (7,7))

#this gets the number of chanels as well
filteredImg = cv2.boxFilter(img , -1 , (5,5))


filteredImg = cv2.GaussianBlur(img, (3,3), 1,1)
#requires square kernel size so put only one dimension
#the best for this type of noise -  if i have more types maybe other filters are better
filteredImg = cv2.medianBlur(img, 3)

cv2.imshow('Filter', filteredImg)
cv2.waitKey(0)