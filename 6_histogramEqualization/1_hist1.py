import cv2
import numpy as np
import matplotlib.pyplot as plt


img = cv2.imread("../photos/lena.png")

color = ("b", "g", "r")
for i, col in enumerate(color):
    # calculates the histogram for the BGR channel
    hist = cv2.calcHist([img], [i], None, [256], [0, 256])
    plt.plot(hist, col)

plt.xlim([0, 256])
plt.show()