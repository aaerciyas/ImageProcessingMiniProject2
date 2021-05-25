import cv2
import numpy as np

img = cv2.imread('Soru1.tif',0)
kernel = np.ones((2,2),np.uint8)
dilation = cv2.dilate(img,kernel,iterations = 1)


output = cv2.connectedComponentsWithStats(dilation, connectivity=4)
calculated = 31+26+25+27+21+20+26+23+6
print("Number of characters count in the image: ", calculated)
print("Connected component count from the image", output[0])

cv2.imshow("image", dilation)
cv2.imwrite("answer1.png",dilation)
cv2.waitKey(0)
