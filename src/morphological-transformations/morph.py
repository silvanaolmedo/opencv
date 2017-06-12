import cv2
import numpy as np

image = cv2.imread('j.png')
kernel = np.ones((5, 5), np.uint8)

cv2.imshow("Original", image)

erosion = cv2.erode(image, kernel, iterations = 1)
cv2.imshow("Erode", erosion)

dilation = cv2.dilate(image, kernel, iterations = 1)
cv2.imshow("Dilate", dilation)

cv2.waitKey(0)
cv2.destroyAllWindows()


