import cv2
import numpy as np

print(cv2.__version__)

face_cascade = cv2.CascadeClassifier('MBS3523 Resources/haarcascade_frontalface_default.xml')
cam = cv2.VideoCapture(0)
font = cv2.FONT_HERSHEY_PLAIN

while True:

            success, img = cam.read()
            imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            imgGray = cv2.cvtColor(imgGray, cv2.COLOR_GRAY2BGR)
            faces = face_cascade.detectMultiScale(img, 1.1, 4)
            for (x, y, w, h) in faces:
             cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 3)
            cv2.putText(img, "MBS3523 Assignment 1c ", (125, 40), cv2.FONT_HERSHEY_PLAIN, 2, (0, 0, 255), 2)
            cv2.putText(img, " Q4 Name: Ho Tsz Sum", (125, 70), cv2.FONT_HERSHEY_PLAIN, 2, (0, 0, 255), 2)



            cv2.imshow('Face', img)


            if cv2.waitKey(1) & 0xff == ord('q'):
                 break

cam.release()
cv2.destroyAllWindows()
