import cv2
import numpy as np
import matplotlib.pyplot as plt
# %matplotlib inline

road = cv2.imread("DATA/road_image.jpg")
road_copy = np.copy(road)
marker_image = np.zeros(road.shape[:2],dtype=np.int32)
segments = np.zeros(road.shape,dtype=np.uint8)
from matplotlib import cm
def create_rgb(i):
    return tuple(np.array(cm.tab10(i)[:3])*255)
colors=[]
for i in range(10):
    colors.append(create_rgb(i))
    
### 
###  Global variables 
n_markers = 10  
current_marker = 1
marks_updated =False

# # Callback functions 

def mouse_callback(event,x,y,flags,param):
    global marks_updated
    
    if event == cv2.EVENT_LBUTTONDOWN:
        marks_updated = True
        # Markers passed to the watershed algo
        cv2.circle(marker_image,(x,y),10,(current_marker),-1)
        # User sees on the Raod Image
        cv2.circle(road_copy,(x,y),10,colors[current_marker],-1)
        
        
        
cv2.namedWindow("Road_Image")
cv2.setMouseCallback("Road_Image",mouse_callback)

while True:
    cv2.imshow("Watershed_Segments",segments)
    cv2.imshow("Road_Image",road_copy)
    
    # Close All Window
    k = cv2.waitKey(1)
    
    if k == 27:
        break
        
    #Clearing all the colors by pressing C Key
    elif k == ord('c'):
        road_copy = road.copy()
        marker_image = np.zeros(road.shape[:2],dtype=np.int32)
        segments = np.zeros(road.shape,dtype=np.uint8)
    # Update color choice
    elif k>0 and chr(k).isdigit():
        current_marker = int(chr(k))
        
    elif marks_updated is True:
        marker_image_copy = marker_image.copy()
        cv2.watershed(road,marker_image_copy)
        
        segments = np.zeros(road.shape,dtype=np.uint8)
    
        for color_ind in range(n_markers):
            segments[marker_image_copy == (color_ind)] = colors[color_ind]
    
cv2.destroyAllWindows()