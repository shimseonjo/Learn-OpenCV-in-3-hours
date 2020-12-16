import cv2
import numpy as np
import imageF
import os
path = os.path.dirname(__file__)

img = cv2.imread(path+'/Resources/lena.png')
imgGray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)


# imgHor = np.hstack((img,img))
imgVer = np.vstack((img,img))
# imgVer = np.vstack((img,imgGray))

imgStack = imageF.stackImages(0.5,([img,imgGray,img],[img,img,img]))

# cv2.imshow("Horizontal",imgHor)
cv2.imshow("Vertical",imgVer)
cv2.imshow("ImageStack",imgStack)

cv2.waitKey(0)