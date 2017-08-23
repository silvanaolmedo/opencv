import cv2
import numpy as np

#Estan inicializadas antes para que el programa no se rompa
radius = 1
r = -1
g = -1
b = -1
#Solo se dibuja el circulo cuando esta variable es true, el valor cambiara dependiendo del evento del mouse
drawing = False

#Funcion que usaremos para se produzca un evento de mouse
def draw_circle(event, x, y, flags, param):
	global drawing
	if event == cv2.EVENT_LBUTTONDOWN:
		drawing = True
	elif event == cv2.EVENT_MOUSEMOVE:
		if drawing:
			cv2.circle(image, (x, y), radius, (b, g, r), -1)
	elif event == cv2.EVENT_LBUTTONUP:
		drawing = False

#Esta funcion es necesaria para los trackbars
def nothing(x):
	pass

#Se crea una imagen de color negro
image = np.zeros((300, 512, 3), np.uint8)
name_window = "Image"
#Seteamos el nombre de la ventana
cv2.namedWindow(name_window)

#Se crean los trackbars dentro de la ventana "Image"
cv2.createTrackbar("R", name_window, 0, 100, nothing)
cv2.createTrackbar("B", name_window, 0, 100, nothing)
cv2.createTrackbar("G", name_window, 0, 100, nothing)
cv2.createTrackbar("Radius", name_window, 1, 50, nothing)

#Seteamos la funcion para la ventana "Image"
cv2.setMouseCallback(name_window, draw_circle)

#Se ejecuta hasta que se apriete Esc
while True:
	cv2.imshow(name_window, image)

	radius = cv2.getTrackbarPos("Radius", name_window)
	r = cv2.getTrackbarPos("R", name_window)
	b = cv2.getTrackbarPos("B", name_window)
	g = cv2.getTrackbarPos("G", name_window)
	
	k = cv2.waitKey(1) 

	if k == 27:
		break

#Al finalizar se destruyen todas las ventanas
cv2.destroyAllWindows()
