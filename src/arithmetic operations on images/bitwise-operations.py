import cv2

img1 = cv2.imread("../images/python_logo.png")
img2 = cv2.imread("../images/gatito.jpg")

height, width = img1.shape[:2]
roi = img2[0:height, 0:width]

img2gray = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
# cv2.imshow("img2gray", img2gray)
# cv2.waitKey(0)
ret, mask = cv2.threshold(img2gray, 10, 255, cv2.THRESH_BINARY)
# cv2.imshow("mask", mask)
# cv2.waitKey(0)
mask_inv = cv2.bitwise_not(mask)
# cv2.imshow("mask_inv", mask_inv)
# cv2.waitKey(0)

img1_bg = cv2.bitwise_and(roi, roi, mask = mask_inv)
# cv2.imshow("img1_bg", img1_bg)
# cv2.waitKey(0)

img2_fg = cv2.bitwise_and(img1, img1, mask = mask)
# cv2.imshow("img2_fg", img2_fg)
# cv2.waitKey(0)

dst = cv2.add(img1_bg, img2_fg)
# cv2.imshow("dst", dst)
# cv2.waitKey(0)
img2[0:height, 0:width] = dst

cv2.imshow("res", img2)
cv2.waitKey(0)
cv2.destroyAllWindows()

