# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import cv2
import dlib
import time

cnn_face_detector=dlib.cnn_face_detection_model_v1('mmod_human_face_detector.dat')

image_location='donald_trump_kim_jong_un.jpg'

image=cv2.imread(image_location)

start=time.time()

faces_cnn=cnn_face_detector(image,1)

end=time.time()

print(format(end-start,'.2f'))

for face in faces_cnn:
    x=face.rect.left()
    y=face.rect.top()
    w=face.rect.right()-x
    h=face.rect.bottom()-y
    
    cv2.rectangle(image,(x,y),(x+w,y+h),(0,255,0),2)

cv2.imshow('image',image)
cv2.waitKey(0)
cv2.destroyAllWindows()    