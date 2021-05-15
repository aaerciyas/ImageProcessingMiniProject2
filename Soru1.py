import cv2
import numpy as np

img = cv2.imread('Soru1.tif',0)
kernel = np.ones((2,2),np.uint8)
dilation = cv2.dilate(img,kernel,iterations = 1)
opening = cv2.morphologyEx(img, cv2.MORPH_OPEN, kernel)
closing = cv2.morphologyEx(img, cv2.MORPH_CLOSE, kernel)

# cv2.imshow("dilation", dilation)
# cv2.imshow("opening", opening)
# cv2.imshow("closing", closing)
# cv2.waitKey(0)

output = cv2.connectedComponentsWithStats(dilation, connectivity=4)
calculated = 31+26+25+27+21+20+26+23+6
print("calculated: ", calculated)
print(output[0])
