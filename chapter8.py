import cv2
import numpy as np
import imageF
import os
path = os.path.dirname(__file__)

# cv2.findContours
# 이미지 Coutours 동일한 색 또는 동일한 색상 강도를 가진 부분의 가장자리 경계를 연결한 선
# 정확한 이미지 Contour를 확보하기 위해 바이너리 이미지를 사용
# 원본 이미지 변경시키므로 복사본 사용이 좋음
# 검은색 배경에서 흰색 물체를 찾는 것과 비슷하므로 찾고자 하는 대상은 흰색으로 배경은 검정색으로 변경

def getContours(img):
    #cv2.RETR_EXTERNAL:이미지의 가장 바깥쪽의 contour만 추출
    #cv2.CHAIN_APPROX_NONE:contour를 구성하는 모든 점을 저장
    contours,hierarchy = cv2.findContours(img,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)
    for cnt in contours:
        area = cv2.contourArea(cnt)
        print(area)
        if area>500:
            #우리가 찾은 Contour(윤곽)을 실제로 그리는 함수
            #(contour를 나타낼 대상이미지,img에 그릴 contour,그릴 인덱스 파라미터(음수 모든윤곽그림),bgr색상,선의두께)
            cv2.drawContours(imgContour, cnt, -1, (255, 0, 0), 3)
            #contour(윤곽)의 호의 길이
            peri = cv2.arcLength(cnt,True)
            #print(peri)
            #approxPolyDP함수는 인자로 주어진 곡선 또는 다각형을 epsilon값에 따라 
            #꼭지점수를 줄여 새로운 곡선이나 다각형을 생성하여 리턴
            #cnt:Numpy Array형식의 곡선 또는 다각형
            #epsilon : 근사값 정확도를 위한 값 
            #True이면 페곡선, False이면 양끝이 열려 있는 곡선임을 의미
            approx = cv2.approxPolyDP(cnt,0.02*peri,True)
            print(len(approx))
            objCor = len(approx)
            #Cv2.BoundingRect(윤곽선 배열)로 최소 크기 사각형을 계산합니다.
            #경계 사각형 함수는 Rect 구조체를 반환합니다.
            x, y, w, h = cv2.boundingRect(approx)

            if objCor ==3: 
                objectType ="Tri"
            elif objCor == 4:
                #정사각형인지 직사각형인지 체크
                aspRatio = w/float(h)
                if aspRatio >0.98 and aspRatio <1.03: objectType= "Square"
                else:objectType="Rectangle"
            elif objCor>4: objectType= "Circles"
            else:objectType="None"



            cv2.rectangle(imgContour,(x,y),(x+w,y+h),(0,255,0),2)
            cv2.putText(imgContour,objectType,
                        (x+(w//2)-10,y+(h//2)-10),cv2.FONT_HERSHEY_COMPLEX,0.7,
                        (0,0,0),2)


path = path +'/Resources/shapes.png'
img = cv2.imread(path)
imgContour = img.copy()

imgGray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
imgBlur = cv2.GaussianBlur(imgGray,(7,7),1)
imgCanny = cv2.Canny(imgBlur,50,50)
getContours(imgCanny)

imgBlank = np.zeros_like(img)
imgStack = imageF.stackImages(0.8,([img,imgGray,imgBlur],
                            [imgCanny,imgContour,imgBlank]))

cv2.imshow("Stack", imgStack)

cv2.waitKey(0)
