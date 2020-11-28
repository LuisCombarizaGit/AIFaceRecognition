######################  AI visual recognition #################
# Luis Combariza Nov 27,2020
# luis_combariza@outlook.com

import cv2
import numpy

# Setting frame
frameWidth = 640
frameHeight = 480
cap = cv2.VideoCapture(0)
cap.set(3, frameWidth)
cap.set(4, frameHeight)
cap.set(10,150)

def findColor(img):
    imgHSV = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)


while True:
    success, img = cap.read()
    cv2.imshow("Result", img)
    if cv2.waitKey(1) and 0xFF == ord('q'):
        break
