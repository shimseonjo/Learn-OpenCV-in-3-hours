import cv2
import numpy as np
import os
path = os.path.dirname(__file__)
img = cv2.imread(path+"/Resources/shapes.png")
print(img.shape)
#높이,넓이
imgResize = cv2.resize(img,(1000,500))
print(imgResize.shape)

imgCropped = img[46:119,352:495]

cv2.imshow("Image",img)
cv2.imshow("Image Resize",imgResize)
cv2.imshow("Image Cropped",imgCropped)

cv2.waitKey(0)