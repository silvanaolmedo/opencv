import cv2
from matplotlib import pyplot as plt

image = cv2.imread('../CannyEdgeDetection/gatito2.jpg')
image = cv2.cvtColor(image,cv2.COLOR_BGR2RGB)
blur = cv2.blur(image,(5,5))
gaussian_blur = cv2.GaussianBlur(image,(5,5),0)
median_blur = cv2.medianBlur(image,5)


plt.subplot(221),plt.imshow(image),plt.title("Original")
plt.xticks([]),plt.yticks([])
plt.subplot(222),plt.imshow(blur),plt.title("Con blur")
plt.xticks([]),plt.yticks([])
plt.subplot(223),plt.imshow(gaussian_blur),plt.title("Con gaussian blur")
plt.xticks([]),plt.yticks([])
plt.subplot(224),plt.imshow(median_blur),plt.title("Con median blur")
plt.xticks([]),plt.yticks([])

plt.show()