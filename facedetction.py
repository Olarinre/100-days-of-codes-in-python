#import opencv library
import cv2

#read the image
# image is read as a numpy array
img = cv2.imread("C:\\Users\\USER\\Desktop\\programming\\python\\opencv\\ay1.jpg", 1)

#print(img)
#face detection part
face_cascade = cv2.CascadeClassifier("C:\\Users\\USER\\Desktop\\programming\\python\\opencv\\haarcascade_frontalface_default.xml")
# convert the img to grayscale
grey_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
faces = face_cascade.detectMultiScale(grey_img, scaleFactor  =1.05, minNeighbors = 5)
print(type(faces))
print(faces)

for x,y,w,h in faces:
    img = cv2.rectangle(img,(x,y), (x+w, y+h),(0,255,0),3)

cv2.imshow("Ayobami", img) #opens a window to sidplay the img
cv2.waitKey(0)# closes the window on prssing any key
cv2.destroyAllWindows()