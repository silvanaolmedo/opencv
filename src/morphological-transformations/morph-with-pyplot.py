import cv2
import numpy as np
from matplotlib import pyplot as plt

image = cv2.imread('j.png')
image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
#kernel = np.ones((5,5), np.uint8)
kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (5,5))
print(kernel)

erosion = cv2.erode(image, kernel, iterations = 1)

dilation = cv2.dilate(image, kernel, iterations = 1)

plt.subplot(131),plt.imshow(image),plt.title("Original")
plt.xticks([]),plt.yticks([])
plt.subplot(132),plt.imshow(erosion),plt.title("Erode")
plt.xticks([]),plt.yticks([])
plt.subplot(133),plt.imshow(dilation),plt.title("Dilate")
plt.xticks([]),plt.yticks([])

plt.show()