import cv2
#import numpy as np

cap = cv2.VideoCapture(0)


while(True):
	ret, frame = cap.read()

	# gray = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

	# cv2.imshow("Frame in gray", gray)
	cv2.imshow("Frame", frame)
	if cv2.waitKey(1) == 27:
		break

cap.release()
cv2.destroyAllWindows()

