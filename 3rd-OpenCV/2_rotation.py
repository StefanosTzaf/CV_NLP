import numpy as np
import cv2

img = cv2.imread('../photos/dnd.jpg')
# πρωτα το υψος!
height, width = img.shape[:2]
print(width)
print(height)
cv2.imshow("Original", img)
cv2.waitKey(0)

#double // for flour division -- center (width ~ height) , angle, scale
M = cv2.getRotationMatrix2D( (width//2.0, height//2.0) , 90, 1)
dst = cv2.warpAffine(img, M, (width, height))
cv2.imshow("Rotated", dst)
cv2.waitKey(0)