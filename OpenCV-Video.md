# Streaming Video Capture with Computer Camera

import cv2

## import camera! 0 = default camera
cap = cv2.VideoCapture(0)

## capture width and height, default is float
width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

#### to write stream to video file ####
# 1. create a writer object 
# fourcc = 4byte code that specifies video codec based on OS
# frames per second (between 20 and 30)
# provide width and height information
writer = cv2.VideoWriter('myvideo.mp4', cv2.VideoWriter_fourcc(*"XVID"),20,(width, height))

# display image
while True:
    
    ret,frame = cap.read()
    

# 2. write each frame to mp4 file
    writer.write(frame)
    
    cv2.imshow('frame', frame)
    
    if cv2.waitKey(1) & 0xFF == 27:
        break
        
# stop capturing video
cap.release()
# 3. release writer
writer.release()
cv2.destroyAllWindows()

<br>
----------------------------------------------------------------------
# Open Video and Watch
import cv2
import time

## open video
cap = cv2.VideoCapture('DATA/finger_move.mp4')

if cap.isOpened() == False:
    print('ERROR FILE NOT FOUND OR WRONG CODEC USED')

while cap.isOpened():
    

    ret,frame = cap.read()
##ret = return, so while returning --> show it, if not --> break    
    if ret == True:
        
## for human viewing, we have to slow video to frame rate         
        time.sleep(1/20)
        cv2.imshow('frame',frame)
        
        if cv2.waitKey(10) & 0xFF == 27:
            break
        
    else:
        break

cap.release()
cv2.destroyAllWindows()
<br>
___________________________________________________________________________________
# Drawing Static Shapes on Video Frames
import cv2

cap = cv2.VideoCapture(0)

width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

## TOP LEFT corner
x = width // 2
y = height // 2

## width and height of RECTANGLE
w = width // 4
h = height // 4

## BOTTOM RIGHT x + w, y + h


while True:
    
    ret,frame = cap.read()
    ## draw rectangle, THEN show frame!    
    ## args = top left, botom right     
    cv2.rectangle(frame,(x,y),(x+w, y+h),color=(0,0,255),thickness=4)
    
    cv2.imshow('frame', frame)
    
    if cv2.waitKey(1) & 0xFF == 27:
        break

cap.release()
cv2.destroyAllWindows()
<br>
___________________________________________________________________________________
# Drawing Dynamic Shapes on Video Frames

import cv2


## CALLBACK FUNCTION RECTANGLE
def draw_rectangle(event,x,y,flags,param):
    
    global pt1, pt2, topLeft_clicked, bottomRight_clicked
    
    if event == cv2.EVENT_LBUTTONDOWN:
        
        ## RESET THE RECTANGLE (checks if retangle is already there!)
        if topLeft_clicked == True and bottomRight_clicked == True:
            pt1 = (0,0)
            pt2 = (0,0)
            topLeft_clicked = False
            bottomRight_clicked = False
            
        if topLeft_clicked == False:
            pt1 = (x,y)
            topLeft_clicked = True
        
        elif bottomRight_clicked == False:
            pt2 = (x,y)
            bottomRight_clicked = True
        
    

## GLOBAL VARIABLES
pt1 = (0,0)
pt2 = (0,0)
topLeft_clicked = False
bottomRight_clicked = False

## CONNECT TO CALLBACK
cap = cv2.VideoCapture(0)

cv2.namedWindow('Test')
cv2.setMouseCallback('Test', draw_rectangle)




while True:
    
    ret,frame = cap.read()
    
    ## DRAWING ON THE FRAME BASED ON GLOBAL VARIABLES    
    if topLeft_clicked:
        cv2.circle(frame,center=pt1,radius=5,color=(0,0,255),thickness=-1)
    
    if topLeft_clicked & bottomRight_clicked:
        cv2.rectangle(frame,pt1,pt2,(0,0,255),3)
   
    cv2.imshow('Test', frame)
    
    if cv2.waitKey(1) & 0xFF == 27:
        break

cap.release()
cv2.destroyAllWindows()
