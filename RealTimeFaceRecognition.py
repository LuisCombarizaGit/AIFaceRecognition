######################  AI FACE recognition #################
# Luis Combariza Nov 27,2020
# luis_combariza@outlook.com

import cv2
import numpy as np
import face_recognition
import os

path = './'
images = []
classNames = []



imgElon = face_recognition.load_image_file("Elon_Musk_One.jpg")
imgElon = cv2.cvtColor(imgElon,cv2.COLOR_BGR2RGB)
imgTest = face_recognition.load_image_file("Elon_Musk_Two.jpeg")
imgTest = cv2.cvtColor(imgTest,cv2.COLOR_BGR2RGB)