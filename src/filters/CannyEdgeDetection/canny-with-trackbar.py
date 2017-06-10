import cv2
import numpy as np

def nothing(x):
	pass

img = cv2.imread('gatito2.jpg');
img_default = img
name_window = "Canny Edge Detection with Trackbars"
cv2.namedWindow(name_window)

cv2.createTrackbar('minVal',name_window,0,1000,nothing)
cv2.createTrackbar('maxVal',name_window,0,2000,nothing)

while(True):
	cv2.imshow(name_window,img)
	k = cv2.waitKey(1) 
	if k == 27:
		break

	minVal = cv2.getTrackbarPos('minVal',name_window)
	maxVal = cv2.getTrackbarPos('maxVal',name_window)

	if(minVal == 0 & maxVal == 0):
		img = img_default
	else:
		img = cv2.Canny(img_default,minVal,maxVal)
	

cv2.destroyAllWindows()

