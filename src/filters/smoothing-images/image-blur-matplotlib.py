import cv2
from matplotlib import pyplot as plt

image = cv2.imread('../CannyEdgeDetection/gatito2.jpg')
image = cv2.cvtColor(image,cv2.COLOR_BGR2RGB)
blur = cv2.blur(image,(5,5))
gaussian_blur = cv2.GaussianBlur(image,(5,5),0)
median_blur = cv2.medianBlur(image,5)


# plt.subplot(121),plt.imshow(image),plt.title("Original")
# plt.xticks([]),plt.yticks([])
plt.subplot(121),plt.imshow(blur),plt.title("Con blur")
plt.xticks([]),plt.yticks([])
plt.subplot(122),plt.imshow(gaussian_blur),plt.title("Con gaussian blur")
plt.xticks([]),plt.yticks([])
# plt.subplot(122),plt.imshow(median_blur),plt.title("Con median blur")
# plt.xticks([]),plt.yticks([])

plt.show()