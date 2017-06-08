import cv2
import numpy as np

img = cv2.imread('gatito.jpg')
cv2.imshow("Original", img)

height, width = img.shape[:2]
img_sized = cv2.resize(img, (width/2, height/2))
cv2.imshow("Resized", img_sized)

#img_warpAff = cv2.warpAffine(img, T, img.shape)

gray = cv2.cvtColor(img_sized, cv2.COLOR_BGR2GRAY)
cv2.imshow("Grises", gray)

blur = cv2.blur(gray, (5,5))
cv2.imshow("Con blur!!", blur)

canny = cv2.Canny(blur, 100, 200)
cv2.imshow("Con Canny!!", canny)

canny2 = cv2.Canny(blur, 100, 400)
cv2.imshow("Con Canny 500!!", canny2)


cv2.waitKey(0)
cv2.destroyAllWindows()