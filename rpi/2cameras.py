import numpy as np
import cv2

cap = cv2.VideoCapture(0)
cap2 = cv2.VideoCapture(2)

while(cap.isOpened()):
    ret, frame = cap.read()
    ret, frame2 = cap2.read()
    
    if ret==True:
        cv2.imshow('frame',frame)
        cv2.imshow('frame2',frame2)
        
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break

# Release everything if job is finished
cap.release()
cap2.release()
cv2.destroyAllWindows()
