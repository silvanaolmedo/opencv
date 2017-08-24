import cv2

image = cv2.imread("../images/python_logo.png")
image2 = cv2.imread("../images/sid_ice_age.jpg")

dst = cv2.addWeighted(image, 0.7, image2, 0.3, 0)

cv2.imshow("Result", dst)
cv2.waitKey(0)
cv2.destroyAllWindows()
