import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

# Load a color image in grayscale
img = cv.imread('soumikfunk.jpeg', 0)

cv.imshow('soumik', img)
cv.waitKey(0)
cv.destroyAllWindows()