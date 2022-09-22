# sample script from Pierian-Data Udemy course
# this script pops out two windows to allow for custom seeding for watershed algorthim as applied to an image
# the purpose is to help computer differentiate between objects and background/foreground

import cv2
import matplotlib.pyplot as plt
import numpy as np
from matplotlib import cm

# read in image and make a copy
img = cv2.imread("filepath")
img = cv2.resize(img, (965,643))
img_copy = np.copy(img)

# create 2 empty spaces
marker_image = np.zeros(img.shape[:2], np.int32)

segments = np.zeros(img.shape, np.uint8)

# create colors for markers
def create_rgb(i):
    x = np.array(cm.tab10(i))[:3] * 255
    return tuple(x)

colors = []

for i in range (10):
    colors.append(create_rgb(i))
    
# set up callback function

# GLOBALS
n_markers = 10
current_marker = 1
marks_updated = False

# FUNCTION
def mouse_callback(event, x, y, flags, param):
    global marks_updated
    
    if event == cv2.EVENT_LBUTTONDOWN:
        cv2.circle(marker_image, (x,y), 10, (current_marker), -1)
        
        cv2.circle(boulders_copy, (x,y), 10, colors[current_marker], -1)
        marks_updated = True

# set up callback function
cv2.namedWindow("windowName")
cv2.setMouseCallback("windowName", mouse_callback)


while True:
    
    cv2.imshow("segments", segments)
    cv2.imshow("windowName", img_copy)
    
    
    k = cv2.waitKey(1)
    
    if k == 27:
        break
    
    elif k == ord('c'):
        img_copy = img.copy()
        marker_image = np.zeros(img.shape[:2], np.int32)
        segments = np.zeros(img.shape, np.uint8)
        
    elif k > 0 and chr(k).isdigit():
        current_marker = int(chr(k))
    
    if marks_updated:
        
        marker_image_copy = marker_image.copy()
        cv2.watershed(img, marker_image_copy)
        
        segments = np.zeros(img.shape, np.uint8)
        
        for color_index in range(n_markers):
            segments[marker_image_copy == (color_index)] = colors[color_index]
            
        marks_updated = False 
        
        
cv2.destroyAllWindows()
