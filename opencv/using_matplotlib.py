import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

img = cv.imread('soumikfunk.jpeg', 0)
plt.imshow(img, cmap='gray', interpolation='bicubic')
# to hide tick values on X and Y axis
plt.xticks([]), plt.yticks([])
plt.show()
