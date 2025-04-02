import cv2
import numpy as np

# Load image in grayscale
img = cv2.imread('../photos/tsukuba.png', 0)    

# Histogram equalization
equalized_img = cv2.equalizeHist(img)

# CLAHE equalization
# Contrast Limited Adaptive Histogram Equalization
# applies histogram equalization to small regions in the image 
# so as to avoid over-amplifying noise, smaller regions like convolution kernels

clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8, 8))
img_clahe = clahe.apply(img)

# Concatenate images horizontally
showImg = np.hstack([img, equalized_img, img_clahe])

# Display image
cv2.imshow('Equalization Comparison', showImg)
cv2.waitKey(0)
cv2.destroyAllWindows()
