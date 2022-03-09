import cv2
import numpy as np

img = np.zeros((800,800,3),np.uint8)

img = cv2.line(img,(0,400),(800,400),(125,255,0),5)
img = cv2.line(img,(400,0),(400,800),(255,0,0),5)

img = cv2.circle(img, (400,400), 50, (0,0,255),3)

img = cv2. rectangle(img,(200,200),(600,600),(0,125,125),5)
cv2.imshow('img', img)
cv2.waitKey(0)