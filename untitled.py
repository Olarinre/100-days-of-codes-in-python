import cv2 as cv

#face detection on the webcam
#this program detects the face on a live webcam.

imgcapture = cv.VideoCapture(0)
face_cascade = cv.CascadeClassifier("C:\\Users\\USER\\Desktop\\programming\\python\\opencv\\haarcascade_frontalface_default.xml")

a =1
while True:
    a+=1
    check,frame = imgcapture.read()
    faces = face_cascade.detectMultiScale(frame, scaleFactor=1.05, minNeighbors=5)
    for x, y, w, h in faces:
        cv.rectangle(frame, (x, y), (x + w, y + h), (0, 200, 0), 3)
    cv.imshow("captured img", frame)

    if cv.waitKey(1) == ord('q'):
        break;
imgcapture.release()
cv.destroyAllWindows()