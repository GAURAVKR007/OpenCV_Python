# Drawing Images --> Part 1

# import cv2
# import numpy as np

# ##############
# ## FUNCTION ##
# ##############

# def draw_circle(event,x,y,flags,param):
#     if event == cv2.EVENT_LBUTTONDOWN:
#         cv2.circle(img,(x,y),radius=100,color=(255,0,0),thickness=-1)
#     elif event == cv2.EVENT_RBUTTONDOWN:
#         cv2.circle(img,(x,y),radius=75,color=(0,0,255),thickness=-1)

# cv2.namedWindow(winname='my_Drawing')
# cv2.setMouseCallback('my_Drawing',draw_circle)

# ################################
# ## SHOWING IMAGE WITH OPENCV ###
# ################################

# img = np.zeros(shape=(512,512,3),dtype=np.int8)

# while True:
#     cv2.imshow('my_Drawing',img)
    
#     if cv2.waitKey(20) & 0xFF == 27:
#         break
        
# cv2.destroyAllWindows()



import cv2
import numpy as np

# Variables 

# True while mouse button down, False while mouse button up
drawing = False
ix = iy = -1

# Function


# Images with Mouse --> Part 2

# def draw_rectangle(event,x,y,flags,param):
#     global ix,iy,drawing
    
#     if event == cv2.EVENT_LBUTTONDOWN:
        
#         drawing = True
#         ix,iy = x,y
        
#     elif event == cv2.EVENT_MOUSEMOVE:
#         if drawing == True:
#             cv2.rectangle(img,(ix,iy),(x,y),(0,0,255),-1)
#     elif event == cv2.EVENT_LBUTTONUP:
#         drawing = False
#         cv2.rectangle(img,(ix,iy),(x,y),(0,0,255),-1)

# # Showing the Image

# img = np.zeros((512,512,3),np.int8)
# cv2.namedWindow(winname='my_drawing')
# cv2.setMouseCallback('my_drawing',draw_rectangle)

# while True:
#     cv2.imshow('my_drawing',img)
    
#     if cv2.waitKey(1) & 0xFF == 27:
#         break
        
# cv2.destroyAllWindows()


# Images Basics Assessment --> Part 3

import cv2
import numpy as np
import matplotlib.pyplot as plt
# %matplotlib inline 

# raw_img = cv2.imread("DATA/dog_backpack.jpg")
# img = cv2.cvtColor(raw_img,cv2.COLOR_BGR2RGB)
# flip_img = cv2.flip(img,0)
# # cv2.rectangle(img,(200,370),(600,720),(255,0,0),10)  # Red Rectangle around Dog Face
# vertices = np.array([[250,750],[430,400],[600,750]],np.int32)
# pts = vertices.reshape((-1,1,2))
# # cv2.polylines(img,[pts],isClosed=True,color=(255,0,0),thickness=10)
# cv2.fillPoly(img,[pts],(255,0,0))
img = cv2.imread("DATA/dog_backpack.jpg")

def draw_circle(event,x,y,flags,param):
    
    if event == cv2.EVENT_RBUTTONDOWN:
        cv2.circle(img,(x,y),radius=70,color=(255,0,0),thickness=10)
        


cv2.namedWindow(winname='dog_img')
cv2.setMouseCallback('dog_img',draw_circle)       
while True:
    cv2.imshow('dog_img',img)
    
    if cv2.waitKey(20) & 0xFF == 27:
        break
        
cv2.destroyAllWindows()

