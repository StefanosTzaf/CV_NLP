import numpy as numpy
import cv2

#with derivative filters we can detect the edges (for example if lines become from one collor to another the function will have an )

img = cv2.imread('../photos/lena.png')

#convert to gray
#i could have done it with cv2.imread with a second parameter cv2.IMREAD_GRAYSCALE
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# which derivative x-axes or y-axes
gradX = cv2.Sobel(gray, -1, 1, 0)
gradY = cv2.Sobel(gray, -1, 0, 1)

#derivative may be negative so we need to convert it to positive and scale it till 255
gradX = cv2.convertScaleAbs(gradX)
gradY = cv2.convertScaleAbs(gradY)

#merge derivatives

grad = cv2.addWeighted(gradX, 0.5, gradY, 0.5, 0)

cv2.imshow('Result', grad)
cv2.waitKey(0)

#computes 2nd derivative of the image
#Εφαρμόζει τον Laplacian operator για να ανιχνεύσει περιοχές με απότομες αλλαγές στην ένταση (δηλαδή ακμές).
abs = cv2.Laplacian(gray, -1, (3,3))
scaled = cv2.convertScaleAbs(abs)

cv2.imshow('Result', scaled)
cv2.waitKey(0)