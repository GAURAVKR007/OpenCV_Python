import cv2

cap = cv2.VideoCapture(0)

width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))  # 1080p
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

# Windows -> *'DVIX'
# Mac or Linux --> *'XVID'
writer = cv2.VideoWriter('mysupervideo.avi',cv2.VideoWriter_fourcc(*'DIVX'),24,(width,height))

while True:
    ret,frame = cap.read()
    
    # Operation (Drawing)
    
    writer.write(frame)
    
#     gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    
    cv2.imshow('frame',frame)
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
        
cap.release()
writer.release()
cv2.destroyAllWindows()