OpenCV with Video!
	*note: when using video, only one kernel open at a time!

Capturing Video Using Webcam

	•	cap = cv2.VideoCapture(0)
		0 = default camera on comp

	•	capture height and width of screen size
	⁃	width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
	⁃	height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
	
	to write stream to video file:

	1.	create writer object
	⁃	writer = cv2.VideoWriter(“name.mp4”, cv2.VideoWriter_fourcc(*”XVID”), 20, (width, height))
	⁃	fourcc = 4byte code, specifying video codec based on OS
	⁃	20 refers to frames per second (20-30 recommended)

	2.	write each frame to mp4 file
	⁃	while True:
	⁃	ret,frame = cap.read()
	⁃	writer.write(frame)
	⁃	cv2.imshow(‘name’, frame)
	⁃	if cv2.waitKey(1) & 0xFF == 27:
	⁃	break
	⁃	# stop capturing video
	⁃	cap.release()

  3.	release writer
	⁃	writer.release()
	⁃	cv2.destroyAllWindows()
		
		
Open and Play Video

import cv2
import time

# open video
cap = cv2.VideoCapture('DATA/finger_move.mp4')
	-note: filepath instead of int representing default camera

if cap.isOpened() == False:
    print('ERROR FILE NOT FOUND OR WRONG CODEC USED')

while cap.isOpened():
    
    ret,frame = cap.read()

#ret = return, so while returning --> show it, if not --> break    
    if ret == True:
        
# for human viewing, we have to slow video to frame rate         
        time.sleep(1/30)
        cv2.imshow('frame',frame)
        
        if cv2.waitKey(10) & 0xFF == 27:
            break
        
    else:
        break

cap.release()
cv2.destroyAllWindows()

Draw Shapes on Live Video (Static)

cap = cv2.VideoCapture(0)

width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

# TOP LEFT corner
x = width // 2
y = height // 2

# width and height of RECTANGLE
w = width // 4
h = height // 4

while True:
    
    ret,frame = cap.read()
    # draw rectangle, THEN show frame!    
    # args = top left, bottom right 
    # BOTTOM RIGHT = x + w, y + h    
    cv2.rectangle(frame,(x,y),(x+w, y+h),color=(0,0,255),thickness=4)
	
    cv2.imshow('frame', frame)
    
    if cv2.waitKey(1) & 0xFF == 27:
        break

cap.release()
cv2.destroyAllWindows()

Draw Shapes on Video (Dynamic)

# CALLBACK FUNCTION RECTANGLE
def draw_rectangle(event,x,y,flags,param):
    
    global pt1, pt2, topLeft_clicked, bottomRight_clicked
    
    if event == cv2.EVENT_LBUTTONDOWN:
        
        # RESET THE RECTANGLE (checks if rectangle is already there!)
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
        
    

# GLOBAL VARIABLES
pt1 = (0,0)
pt2 = (0,0)
topLeft_clicked = False
bottomRight_clicked = False

# CONNECT TO CALLBACK
cap = cv2.VideoCapture(0)

cv2.namedWindow('Test')
cv2.setMouseCallback('Test', draw_rectangle)

while True:
    
    ret,frame = cap.read()
    
    # DRAWING ON THE FRAME BASED ON GLOBAL VARIABLES    
    if topLeft_clicked:
        cv2.circle(frame,center=pt1,radius=5,color=(0,0,255),thickness=-1)
    
    if topLeft_clicked & bottomRight_clicked:
        cv2.rectangle(frame,pt1,pt2,(0,0,255),3)
   
    cv2.imshow('Test', frame)
    
    if cv2.waitKey(1) & 0xFF == 27:
        break

cap.release()
cv2.destroyAllWindows()







