import cv2
import numpy as np

cap = cv2.VideoCapture('Official Opening Credits_ Game of Thrones (HBO).mp4')
while(cap.isOpened()):
	ret, frame = cap.read()
	rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
	cv2.imshow("Intro GoT", rgb)
	if cv2.waitKey(25) == 27:
		break

cap.release()
cv2.destroyAllWindows()