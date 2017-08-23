import cv2
import numpy as np

image = cv2.imread("../images/gatito.jpg")

#Parameters:
#src: input image
#top, bottom, left, right - border width in number of pixels in corresponding directions
#Para estos tipos de bordes no va el value
#borderType - Flag defining what kind of border to be added. It can be following types
#	cv2.BORDER_CONSTANT - Adds a constant colored border. The value should be given as next argument.
#	cv2.BORDER_REFLECT - Border will be mirror reflection of the border elements, like this : fedcba|abcdefgh|hgfedcb
#	cv2.BORDER_REFLECT_101 or cv2.BORDER_DEFAULT - Same as above, but with a slight change, like this : gfedcb|abcdefgh|gfedcba
#	cv2.BORDER_REPLICATE - Last element is replicated throughout, like this: aaaaaa|abcdefgh|hhhhhhh
#	cv2.BORDER_WRAP Cant explain, it will look like this : cdefgh|abcdefgh|abcdefg
#value - Color of border if border type is BORDER_CONSTANT


replicate = cv2.copyMakeBorder(image,10,10,10,10,cv2.BORDER_REPLICATE)
reflect = cv2.copyMakeBorder(image,10,10,10,10,cv2.BORDER_REFLECT)
reflect101 = cv2.copyMakeBorder(image,10,10,10,10,cv2.BORDER_REFLECT_101)
wrap = cv2.copyMakeBorder(image,10,10,10,10,cv2.BORDER_WRAP)
#Va con value porque el tipo es BORDER_CONSTANT
color = (145, 205, 0)
constant = cv2.copyMakeBorder(image, 10, 10, 10, 10, cv2.BORDER_CONSTANT, value = color)

cv2.imshow("Image with replicate border", replicate)
cv2.imshow("Image with reflect border", reflect)
cv2.imshow("Image with reflect101 border", reflect101)
cv2.imshow("Image with wrap border", wrap)
cv2.imshow("Image with constant border", constant)
cv2.waitKey(0)
cv2.destroyAllWindows()