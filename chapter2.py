import cv2
import numpy as np
import os
path = os.path.dirname(__file__)

img = cv2.imread(path+"/Resources/lena.png")
kernel = np.ones((5,5),np.uint8)

imgGray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
imgBlur = cv2.GaussianBlur(imgGray,(7,7),0)
#cv2.Canny(원본 이미지, 임계값1, 임계값2, 커널 크기, L2그라디언트)
#임계값1 이하에 포함된 가장자리는 가장자리에서 제외
#임계값2 이상에 포함된 가장자리는 가장자리로 간주
imgCanny = cv2.Canny(img,150,200)
#이미지 팽창(두꺼워짐)
imgDialation = cv2.dilate(imgCanny,kernel,iterations=1)
#이미지 침식(가늘어짐)
imgEroded = cv2.erode(imgDialation,kernel,iterations=1)

cv2.imshow("Gray Image",imgGray)
cv2.imshow("Blur Image",imgBlur)
cv2.imshow("Canny Image",imgCanny)
cv2.imshow("Dialation Image",imgDialation)
cv2.imshow("Eroded Image",imgEroded)
cv2.waitKey(0)