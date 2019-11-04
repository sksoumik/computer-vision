import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

# create a blank image
img = np.zeros((512, 512, 3), np.uint8)

# Draw a diagonal blue line with thickness of 5 px
# openCV reads color in BGR format, not in RGB
cv.line(img, (0, 0), (511, 511), (255, 0, 0), 5)

# Drawing rectangle
cv.rectangle(img, (384, 0), (510, 128), (0, 255, 0), 3)
# Drawing a circle
cv.circle(img, (447, 63), 63, (0, 0, 255), -1)

# Drawing Ellipse
cv.ellipse(img, (256, 256), (100, 50), 0, 0, 180, 255, -1)

font = cv.FONT_HERSHEY_SIMPLEX
cv.putText(img,'Soumik',(10,500), font, 4,(255,255,255),2,cv.LINE_AA)


cv.imshow('soumik', img)

k = cv.waitKey(0) & 0xFF

if k == 27:
    cv.destroyAllWindows()
elif k == ord('s'):
    cv.imwrite('newimage.png', img)
    cv.destroyAllWindows()