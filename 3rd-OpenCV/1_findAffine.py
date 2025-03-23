import numpy as np
import cv2

img = cv2.imread('../photos/lena.png')
height, width = img.shape[:2]
cv2.imshow("Original", img)
cv2.waitKey(0)


pts_1 = np.float32([[135, 45], [385, 45], [135, 230]])
pts_2 = np.float32([[135, 45], [385, 45], [150, 230]])
M = cv2.getAffineTransform(pts_1, pts_2)

dst = cv2.warpAffine(img, M, (1024, 1024))
cv2.imshow("Affine Transformation", dst)
cv2.waitKey(0)