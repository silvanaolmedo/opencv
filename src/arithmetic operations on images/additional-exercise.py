import cv2
import numpy as np

#primer leer las dos imagenes
#crear una ventana con un nombre
#agregar trackbars para alfa, beta, landa
# 	dst = alfa * img1 + beta * img2 + lambda
alpha_slider_max = 100
alpha_slider = 0

def nothing(x):
	pass


img1 = cv2.imread("../images/python_logo.png")
img2 = cv2.imread("../images/sid_ice_age.jpg")

window_name = "Image blending"
cv2.namedWindow(window_name)

cv2.createTrackbar("alfa", window_name, alpha_slider, alpha_slider_max, nothing)

while True:
	
	alphaAux = cv2.getTrackbarPos("alfa", window_name)
	alpha = float(alphaAux) / float(alpha_slider_max)
	beta = (1.0 - alpha)
	dst = cv2.addWeighted(img1, alpha, img2, beta, 0)
	cv2.imshow(window_name, dst)
	k = cv2.waitKey(1)
	if k == 27:
		break

cv2.destroyAllWindows()



