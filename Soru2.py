import cv2
import numpy as np
from numpy import ndarray

img = cv2.imread('Soru2.tif',0)
# global thresholding
ret1,th1 = cv2.threshold(img,200,255,cv2.THRESH_BINARY)
cv2.imshow("threshold", th1)
kernel = np.ones((5,5),np.uint8)
erosion = cv2.erode(th1,kernel,iterations = 1)
output = cv2.connectedComponentsWithStats(erosion, connectivity=4)

count = 0
for i in range(output[0]-1):
    print(output[2][i])
    if output[2][i][4] > 300:
        count += 1
print(count)
cv2.imshow("asd",erosion)
cv2.waitKey(0)
