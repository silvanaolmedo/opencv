import cv2
import numpy as np

image = cv2.imread('../CannyEdgeDetection/gatito2.jpg')
cv2.imshow("Original",image)

blur = cv2.blur(image,(5,5))
cv2.imshow("Con blur",blur)

cv2.waitKey(0)
cv2.destroyAllWindows()