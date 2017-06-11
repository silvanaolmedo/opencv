import cv2
import numpy as np
from matplotlib import pyplot as plt

image = cv2.imread('../gatito.jpg')
image = cv2.cvtColor(image,cv2.COLOR_BGR2RGB);

#Aplico filter2D a la imagen 
filter2d = cv2.filter2D(image,-1,(5,5))

plt.subplot(121),plt.imshow(image),plt.title('Original')
plt.xticks([]),plt.yticks([])
plt.subplot(122),plt.imshow(filter2d),plt.title('Image with filter2D')
plt.xticks([]),plt.yticks([])
plt.show()


