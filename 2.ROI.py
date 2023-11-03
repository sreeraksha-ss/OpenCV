import numpy as np
import matplotlib.pyplot as plt
import cv2

original_image = cv2.imread("D:\\Downloads\\cameraman.tif")
print(f" size of the image is {original_image.shape}")
plt.imshow(original_image)
plt.show()

white_area=original_image.copy()

'''
Below lines are used to work on ROI
'''

x1,y1 = 181,62
x2,y2 = 267,172

ROI_area=original_image[62:172, 181:267]
""" selecting region to make it white"""

white_area[62:172, 181:267] = 255

'''
Selecting area to fill
'''
original_image[80:190, 350:436] = ROI_area

plt.subplot(1, 3, 1)
plt.imshow(original_image)

plt.subplot(1, 3, 2)
plt.imshow(ROI_area)

plt.subplot(1, 3, 3)
plt.imshow(white_area)

plt.show()
cv2.waitKey()
cv2.destroyAllWindows()