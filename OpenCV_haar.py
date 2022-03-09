import cv2

cam = cv2.VideoCapture(0)

while True:
            unuse, img = cam.read()
            #print(img.shape)
            #img[100:200, 100:200] = 180
            imgCrop = img[100:300, 300:500]
            imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            imgGray = cv2.cvtColor(imgGray, cv2.COLOR_BGR2GRAY)
            imgGray[100:300, 300:500] = imgCrop

            cv2.putText(img, "Sampson", (125, 225), cv2.FONT_HERSHEY_PLAIN, 2, (0, 0, 255), 2)
            cv2.imshow('img', img)
            cv2.imshow('imgGray', imgGray)
            cv2.imshow('imgCrop', imgCrop)

            if cv2.waitkey(5) & 0xff == 27:
                 break

cam.release()
cv2.destroyAllWindows()