import numpy as np
import cv2
print(cv2.__version__)

original_image = cv2.imread("D:\\Downloads\\cameraman.tif")
print(f" size of the image is {original_image.shape}")

'''
Below lines are used to resize the function
'''

resized_image=cv2.resize(original_image,(250,250))
print(f" size of the image is {resized_image.shape}")

cv2.imshow("original",original_image)
cv2.imshow("resized",resized_image)
cv2.waitKey()
cv2.destroyAllWindows()