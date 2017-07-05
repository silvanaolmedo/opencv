import cv2
import numpy as np

def nothing(x):
	pass

image = np.zeros((300, 512, 3), np.uint8)
name_window = "Image"
cv2.namedWindow(name_window)

cv2.createTrackbar("R", name_window, 0, 255, nothing)
cv2.createTrackbar("G", name_window, 0, 255, nothing)
cv2.createTrackbar("B", name_window, 0, 255, nothing)

while True:
	cv2.imshow(name_window, image)
	key = cv2.waitKey(1)

	if key == 27:
		break

	r = cv2.getTrackbarPos("R", name_window)
	g = cv2.getTrackbarPos("G", name_window)
	b = cv2.getTrackbarPos("B", name_window)
	if r > 0 or g > 0 or b > 0:
		image[:] = [b, g, r]

cv2.destroyAllWindows()

