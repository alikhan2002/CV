import cv2
import numpy as np

################
### FUNCTION ###
################
drawing = False
ix,iy = -1,-1

def draw_rectangle(event,x,y,flags,param):
    
    global ix,iy,drawing
    
    if event == cv2.EVENT_LBUTTONDOWN:
        
        drawing = True
        ix,iy = x,y
        
    elif event ==cv2.EVENT_MOUSEMOVE:
        if drawing == True:
            cv2.rectangle(img,(ix,iy),(x,y),(0,0,255),-1)
            
    elif event == cv2.EVENT_LBUTTONUP:
        drawing = False
        cv2.rectangle(img,(ix,iy),(x,y),(0,0,255),-1)
        

cv2.namedWindow(winname='my_frame')

cv2.setMouseCallback('my_frame',draw_rectangle)

#################################
### SHOWING IMAGE WITH OPENCV ###
#################################

img = np.zeros((512,512,3), np.uint8)

while True:
    
    cv2.imshow('my_frame', img)
    
    if cv2.waitKey(20) & 0xFF == 27:
        break

cv2.destroyAllWindows()