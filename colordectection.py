import cv2 as cv
import numpy as np
#i am still working on sharpening my skillsets
#will modify this to become very better as i progress.
#create video object

vid = cv.VideoCapture(0)

while True:
    check, frame = vid.read()
    #convert frame to hsv from bgr
    hsv_frame = cv.cvtColor(frame, cv.COLOR_BGR2HSV)
    h,w,_ = frame.shape
    #print(h,w)

#define the center of screen as position of color detection
    cx = int(h/2)
    cy = int(w/2)

    center_point = hsv_frame[cy,cx]
    hue_value = center_point[0]
    color ="undefined"
    if hue_value < 4:
        color = "red"
    elif hue_value < 22:
        color = "orange"
    elif hue_value <33:
        color =" yellow"
    elif hue_value <78:
        color="green"
    elif hue_value < 131:
        color ="blue"
    elif hue_value < 178:
        color = "violet"
    else:
        color ="red"
    #print(center_point)
    cv.circle(frame,(cx,cy),5,(0,0,255),3)
    cv.putText(frame,color,(10,50),0,1,(0,0,255),2)
    cv.imshow("detection window", frame)




    if cv.waitKey(1) == ord('q'):
        break;
vid.release()
cv.destroyAllWindows()

