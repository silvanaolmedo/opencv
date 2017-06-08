import cv2
import numpy as np

#Lee imagen gatito.jpg
img = cv2.imread('gatito.jpg')
#Muestra imagen gatito
cv2.imshow("Original", img)

#Define una alto y largo para la imagen
height, width = img.shape[:2]
img_sized = cv2.resize(img, (width/2, height/2))
cv2.imshow("Resized", img_sized)

translation_matrix = np.float32([[1,0,70],[0,1,100]])
img_warpAff = cv2.warpAffine(img_sized, translation_matrix, (width/2, height/2))
cv2.imshow("Translation", img_warpAff)


cv2.waitKey(0)
cv2.destroyAllWindows()