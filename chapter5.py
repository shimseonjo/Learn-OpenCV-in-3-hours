import cv2
import numpy as np
import os
path = os.path.dirname(__file__)

img = cv2.imread(path+"/Resources/cards.jpg")

width,height = 250,350
pts1 = np.float32([[111,219],[287,188],[154,482],[352,440]])
pts2 = np.float32([[0,0],[width,0],[0,height],[width,height]])
#Perspective(원근법) 변환은 직선의 성질만 유지가 되고, 선의 평행성은 유지가 되지 않는 변환
#변환 행렬을 구하기 위해서는 cv2.getPerspectiveTransform() 함수가 필요하며, 
# cv2.warpPerspective() 함수에 변환행렬값을 적용하여 최종 결과 이미지를 얻을 수 있습니다.
matrix = cv2.getPerspectiveTransform(pts1,pts2)
imgOutput = cv2.warpPerspective(img,matrix,(width,height))


cv2.imshow("Image",img)
cv2.imshow("Output",imgOutput)

cv2.waitKey(0)