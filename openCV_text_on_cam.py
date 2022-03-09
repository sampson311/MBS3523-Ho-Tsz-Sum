import cv2
print(cv2.__version__)

x, y = 300,300
dx, dy = 3, 2
cam = cv2.VideoCapture(0)

cam.set(3,600)
cam.set(4,480)

x = 0
dx = 1

while True:

          success, frame = cam.read()

          cv2.rectangle(frame, (x, y), (x + 100 , y+100), (0, 125, 125), 3)
          cv2.putText(frame, "Sampson", (x, y), cv2.FONT_HERSHEY_PLAIN, 2,(0,0,255),2)

          x += dx
          y += dy

          if x >= 560 or x <=0:
             dx *= -1
          if y >= 400 or y <= 0:
              dy *= -1





          cv2.imshow('MBS3523', frame)

          if cv2.waitKey(5) & 0xff == ord('q'):


                 break





cam.release()
cv2.destroyAllWindows()
