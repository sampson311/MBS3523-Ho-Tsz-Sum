import cv2
import numpy as np
print(cv2.__version__)

img = cv2.imread('MBS3523 Resources/lena.png')
img1 = cv2.resize(img, (int(img.shape[1]/1.5), int(img.shape[0]/1.5)))
img2 = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
img3 = cv2.GaussianBlur(img2, (5,5), 0)

cv2.imshow('LENA', img)
cv2.imshow('small LENA', img1)
cv2.imshow('Gary LENA', img2)
cv2.imshow('Bao LENA', img3)

cv2.waitKey(0)