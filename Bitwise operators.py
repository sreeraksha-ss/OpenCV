import numpy as np
import cv2

Original_image = np.zeros((512, 512, 3), dtype=np.uint8)
Original_image = cv2.rectangle(Original_image,(256,0),(512,512),(255, 255, 255), -1)

test = np.zeros((512, 512, 3), dtype=np.uint8)
test = cv2.rectangle(test, (0, 0), (512, 512), (255, 255, 255), -1)

#bitwise AND

bit_AND = cv2.bitwise_and(test, Original_image)
cv2.imshow('AnD', bit_AND)

#bitwise OR

bit_OR=cv2.bitwise_or(test, Original_image)
cv2.imshow('OR', bit_OR)

#bitwise XOR

bit_XOR=cv2.bitwise_xor(test, Original_image)
cv2.imshow('XOR', bit_XOR)

#bitwise XOR

bit_NOT=cv2.bitwise_not(test, Original_image)
cv2.imshow('NOT', bit_NOT)



cv2.imshow ("original", Original_image)
cv2.imshow("test", test)
cv2.waitKey()
cv2.destroyAllWindows()
