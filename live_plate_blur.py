# sample code from a Pierian-Date Udemy project. this uses a cv2 haar cascade trained for recognizing russian license plates.
# In my version, I screen recorded a video of russian dashcam footage from youtube. 

import cv2
import time

plate_rect = cv2.CascadeClassifier("xml filepath")

def plate_rectangle(img):
    
    plate_copy = img.copy()
    
    plate_rects = plate_rect.detectMultiScale(plate_copy, scaleFactor=1.2, minNeighbors=10)
    
    for (x,y,w,h) in plate_rects:
        plate_slice = plate_copy[y:y+h, x:x+w]
    
    plate_blur = cv2.medianBlur(plate_slice, 35)
    
    plate_copy[y: y + plate_blur.shape[0], x: x + plate_blur.shape[1]] = plate_blur
        
    return plate_copy


cap = cv2.VideoCapture("DATA/russianplate.mov")

while cap.isOpened():
    
    ret, frame = cap.read()
    
    frame = plate_rectangle(frame)
    
    if ret == True:
        
        time.sleep(1/30)
        cv2.imshow("Video", frame)
        
        k = cv2.waitKey(1)
        
        if k == 27:
            break
    else:
        break
        
cap.release()
cv2.destroyAllWindows()
