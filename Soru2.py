import cv2
import numpy as np

img = cv2.imread('Soru2.tif',0)
# global thresholding
ret1,th1 = cv2.threshold(img,200,255,cv2.THRESH_BINARY)
#show tresholded image
cv2.imshow("threshold", th1)
#create a 5x5 kernal component
kernel = np.ones((5,5),np.uint8)
# erode component 1 time and look for 8 connectivity
erosion = cv2.erode(th1,kernel,iterations = 1)
output = cv2.connectedComponentsWithStats(erosion, connectivity=8)
#counter for identifical pixel count
count = 0
#for each connected component
print("Connected \t\t Num of\nComponent \t\t  Pixel")
for i in range(output[0]-1):
    print(i+1, "\t\t\t\t", output[2][i][4])
    # if pixel is bigger than it is identical
    if output[2][i][4] > 100:
        count += 1
print("\n\nNumber of identical component count is ",count)
cv2.imshow("erosion",erosion)
cv2.imwrite("answer2-erosion.png", erosion)
cv2.imwrite("answer2-threshold.png",th1)
cv2.waitKey(0)
