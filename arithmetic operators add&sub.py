import cv2
import matplotlib.pyplot as plt

img1 = cv2.imread("D:\\Downloads\\3.jpeg")
img2 = cv2.imread("D:\\Downloads\\2.jpg")

img1 = cv2.resize(img1, (512, 512))
img2 = cv2.resize(img2, (512, 512))

'''
Code to add and display images
'''

AddedImage = cv2.addWeighted(img1, 0.3, img2, 0.7, gamma=0.5)  # gamma relates to brightness

'''
code to subtract and display Images
'''

SubImage = cv2.subtract(img1, img2)

'''
code tpo plot all images 
'''


plt.subplot(1, 4, 1)
plt.title("Hotel")
plt.imshow(img1)

plt.subplot(1, 4, 2)
plt.title("Forest")
plt.imshow(img2)

plt.subplot(1, 4, 3)
plt.title("ForestHotel")
plt.imshow(AddedImage)

plt.subplot(1, 4, 4)
plt.title("HorrorHotel")
plt.imshow(SubImage)

plt.show()
if cv2.waitKey() & 0Xff == 25:
    cv2.destroyAllWindows()
