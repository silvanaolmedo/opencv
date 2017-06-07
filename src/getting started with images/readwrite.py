import cv2

image = cv2.imread("gatito.jpg");
cv2.imshow("Gatito",image);

blur = cv2.GaussianBlur(image, (5,5), 0);
cv2.imshow("Con blur!!", blur);

gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY);
cv2.imshow("Grises", gray);

canny = cv2.Canny(blur, 100, 200);
cv2.imshow("Con Canny!!", canny);

#ret, thresh = cv2.threshold(gray,150,255,cv2.THRESH_BINARY)
#cv2.imshow("Threshold (binary)", thresh)

cv2.waitKey(0);
cv2.destroyAllWindows();
