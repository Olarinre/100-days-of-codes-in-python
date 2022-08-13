import cv2, time

vid = cv2.VideoCapture(0)
a =1

while True:
    a+=1
    check, frame = vid.read()
    #print(frame)
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    cv2.imshow("capturd", gray)
    key = cv2.waitKey(1)
    if key == ord('q'):
        break
print(a)
vid.release()
cv2.destroyAllWindows()