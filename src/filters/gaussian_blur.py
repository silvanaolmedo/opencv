import cv2
import numpy as np

img = cv2.imread('gatito.jpg')
cv2.imshow("sin blur!!", img)

#blur = cv2.blur(img, (5,5))
blur = cv2.GaussianBlur(img, (5,5), 0)

cv2.imshow("Con blur!!", blur)
cv2.waitKey(0)
cv2.destroyAllWindows()

