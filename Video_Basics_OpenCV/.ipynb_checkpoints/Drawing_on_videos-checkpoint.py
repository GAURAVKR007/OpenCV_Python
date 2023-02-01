# import cv2

# cap = cv2.VideoCapture(0)

# width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
# height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

# # Top Left Corner
# x = width // 2
# y = height // 2

# # width and height of Rectanle 
# w = width // 4
# h = height // 4

# # Bottom Right x+w , y+h

# while True:
    
#     ret,frame = cap.read()
#     cv2.rectangle(frame,(x,y),(x+w,y+h),color=(0,0,255),thickness=4)
#     cv2.imshow('frame',frame)
    
#     if cv2.waitKey(1) & 0xFF == ord('q'):
#         break
    
# cap.release()
# cv2.destroyAllWindows()



############ Draw on Live Video ##############

# import cv2



## Callback Function Rectangle 

# def draw_rectangle(event,x,y,flag,param):
    
#     global pt1,pt2,topLeft_clicked,bottomRight_clicked
    
#     if event == cv2.EVENT_LBUTTONDOWN:
        
#         # Reset 
#         if topLeft_clicked and bottomRight_clicked:
#             pt1 = (0,0)
#             pt2 = (0,0)
#             topLeft_clicked = False
#             bottomRight_clicked = False
            
#         if topLeft_clicked == False:
#             pt1 = (x,y)
#             topLeft_clicked = True
#         elif bottomRight_clicked == False:
#             pt2 = (x,y)
#             bottomRight_clicked = True
            

# ## Global variables
# pt1 = (0,0)
# pt2 = (0,0)

# topLeft_clicked = False
# bottomRight_clicked = False

# ## Connect to the Callback

# cap = cv2.VideoCapture(0)

# cv2.namedWindow('Test')
# cv2.setMouseCallback('Test',draw_rectangle)

# while True:
    
#     ret,frame = cap.read()
    
#     # Drawing on the Frames based on the global variables
#     if topLeft_clicked == True:
#         cv2.circle(frame,center=pt1,radius=5,color=(0,0,255),thickness=-1)
#     if topLeft_clicked and bottomRight_clicked:
#         cv2.rectangle(frame,pt1,pt2,(0,0,255),3)
   
#     cv2.imshow('Test',frame)
    
#     if cv2.waitKey(1) & 0xFF == ord('q'):
#         break
    
# cap.release()
# cv2.destroyAllWindows()

########## Video Basics Assessment #############

import cv2


def draw_circle(event,x,y,flags,param):
    
    global pt1,isleftClicked
    
    if event == cv2.EVENT_LBUTTONDOWN:
        pt1 = (x,y)
        isleftClicked = False
        
    if event == cv2.EVENT_LBUTTONUP:
        isleftClicked = True

pt1 = (0,0)

isleftClicked = False

cv2.namedWindow('Test')
cv2.setMouseCallback('Test',draw_circle)



cap = cv2.VideoCapture(0)

while True:
    ret,frame = cap.read()
    
    if isleftClicked:
        cv2.circle(frame,center=pt1,radius=75,color=(0,0,255),thickness=4)
    
    cv2.imshow('Test',frame)
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
        
cap.release()
cv2.destroyAllWindows()