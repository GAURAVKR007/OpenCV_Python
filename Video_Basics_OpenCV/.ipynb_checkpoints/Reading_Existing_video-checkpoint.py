import cv2
import time


cap = cv2.VideoCapture('mysupervideo.avi')

if cap.isOpened() == False:
    print("Error File not Found or Wrong Codec Used")

while cap.isOpened():
    ret,frame = cap.read()
    
    if ret == True:
        
        # Writer 24 FPS
        time.sleep(1/24)      # For human watching Only
        cv2.imshow('frame',frame)
        
        if cv2.waitKey(10) & 0xFF == ord('q'):
            break
    else:
        break
        
cap.release()
cv2.destroyAllWindows()