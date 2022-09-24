import cv2
import numpy as np

# track objects by corner dectection, set up params
corner_params = dict(maxCorners=100,qualityLevel=0.3,minDistance=7,blockSize=7)

# params for Lucas-Kanade Optical Flow Function
# winSize: smaller: tracks more sensitive movements but may miss large movements; larger: opposite
# maxLevel = allows to find optical flow at various resolutions, "image pyramid"
#     0 = original image, 1= 1/2 resolution, 2 = 1/4 resolution etc...
# criteria: 2 methods, whichever is satisifed first, .03 accuracy or 10 iterations, speed vs. accuracy!
# TERM_CRITERIA_EPS: "epsilon criteria", designated accuracy target, so .03 = 1/30th of a pixel
# TERM_CRITERIA_COUNT: iterations; more exhaustive search for points
lk_params = dict(winSize = (200,200), maxLevel = 2, criteria = (cv2.TERM_CRITERIA_EPS | cv2.TERM_CRITERIA_COUNT,10,0.03))
                 

# grab image from camera
cap = cv2.VideoCapture(0)
# first frame will be considered previous frame                 
ret, prev_frame = cap.read()

# grab grayscale version of prev_frame
gray_prev = cv2.cvtColor(prev_frame, cv2.COLOR_BGR2GRAY)

# grab points we want to track, top 10 corners
# ** indicates params passed as dictionary
prev_pts = cv2.goodFeaturesToTrack(gray_prev, mask=None, **corner_params)

# create mask on top of screen to draw lines
# zeros_like creates duplicate of screen with 0's
mask = np.zeros_like(prev_frame)

while True:
    # current frame     
    ret, frame = cap.read()
    
    # create grayscale of live frame
    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    # calculate optical flow on gray_frame
    # LK Optical Flow Function returns, nextPts, status and err    
    # func takes: previous image, current image, prev points to track, next points = None bc we want that returned, params
    
    nextPts, status, err = cv2.calcOpticalFlowPyrLK(gray_prev, gray_frame, prev_pts, None, **lk_params)
    
    # status outputs status vector; each element of vector is set to 1 if flow of corresponding features has been found
    # otherwise: 0
    good_new = nextPts[status == 1]
    good_prev = prev_pts[status == 1]
    
    for i, (new,prev) in enumerate(zip(good_new,good_prev)):
        # iterate through good points, flatten them out     
        x_new , y_new = new.ravel()
        
        x_prev , y_prev = prev.ravel()
        
        # draw lines on mask between previous points and new points
        mask = cv2.line(mask, (int(x_new),int(y_new)), (int(x_prev),int(y_prev)), (0,255,0), 3)
        
        # draw dot where current point we are tracking exists, on current frame
        frame = cv2.circle(frame, (int(x_new),int(y_new)), 8, (0,0,255), -1)
   
    # adds together frame with circles and mask with lines         
    img = cv2.add(frame, mask)
    
    cv2.imshow("Track Me", img)
    
    k = cv2.waitKey(30)
    
    if k == 27:
        break
    
    # update current frame to be previous frame in next iteration!
    gray_prev = gray_frame.copy()
    # how this must be formated to be accepted into LK function
    prev_pts = good_new.reshape(-1,1,2)
    
cap.release()
cv2.destroyAllWindows()
