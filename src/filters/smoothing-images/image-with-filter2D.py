import cv2
import numpy as np

image = cv2.imread('../gatito.jpg')

height, width = image.shape[:2]
image_resized = cv2.resize(image,(width/2,height/2))

cv2.imshow("Original",image_resized)

filter2d = cv2.filter2D(image_resized,-1,(5,5))
cv2.imshow("Image with filter2D",filter2d)

cv2.waitKey(0)
cv2.destroyAllWindows()