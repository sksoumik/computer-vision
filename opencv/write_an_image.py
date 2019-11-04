import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

img = cv.imread('soumikfunk.jpeg', 0)
cv.imshow('soumik', img)

k = cv.waitKey(0) & 0xFF

if k == 27:
    cv.destroyAllWindows()
elif k == ord('s'):
    cv.imwrite('newimage.png', img)
    cv.destroyAllWindows()
