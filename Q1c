import cv2
print(cv2.__version__)

faceCascade = cv2.CascadeClassifier('MBS3523 Resources/haarcascade_frontalface_default.xml')
capture = cv2.VideoCapture(0)
capture.set(3,640)
capture.set(4,480)

font = cv2.FONT_HERSHEY_PLAIN

while True:
    success, img = capture.read()
    cv2.putText(img, "MBS3523 Assignment 1c ", (125, 40), cv2.FONT_HERSHEY_PLAIN, 2, (0, 0, 255), 2)
    cv2.putText(img, " Q4 Name: Ho Tsz Sum", (125, 70), cv2.FONT_HERSHEY_PLAIN, 2, (0, 0, 255), 2)
    imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    imgGray = cv2.cvtColor(imgGray, cv2.COLOR_GRAY2BGR)
    faces = faceCascade.detectMultiScale(imgGray, 1.2, 10)
    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)
        roiImg = img[y:y + h, x:x + w].copy()
        imgGray[y:y + h, x:x + w] = roiImg

    cv2.imshow('Haar', imgGray)

    if cv2.waitKey(1) == ord('q'):
        break

capture.release()
cv2.destroyAllWindows()
