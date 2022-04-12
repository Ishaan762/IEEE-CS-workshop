import cv2
import numpy as np
from matplotlib import pyplot as plt

# reading image
img = cv2.imread("C:\\Users\\Ishaan\\Desktop\\IEEEsample1.png")


gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
 
blur = cv2.GaussianBlur(gray, (5, 5),cv2.BORDER_DEFAULT)
ret, thresh = cv2.threshold(blur, 200, 255,cv2.THRESH_BINARY_INV)

contours, hierarchies = cv2.findContours(thresh, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)

blank = np.zeros(thresh.shape[:2],dtype='uint8')

cv2.drawContours(blank, contours, -1,(255, 0, 0), 1)
c=0
cv2.imwrite("Contours.png", blank)
# Convert the imageFrame in 
    # BGR(RGB color space) to 
    # HSV(hue-saturation-value)
    # color space
hsvFrame = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
  
    # Set range for red color and 
    # define mask
red_lower = np.array([136, 87, 111], np.uint8)
red_upper = np.array([180, 255, 255], np.uint8)
red_mask = cv2.inRange(hsvFrame, red_lower, red_upper)
  
    # Set range for green color and 
    # define mask
green_lower = np.array([25, 52, 72], np.uint8)
green_upper = np.array([102, 255, 255], np.uint8)
green_mask = cv2.inRange(hsvFrame, green_lower, green_upper)
  
    # Set range for blue color and
    # define mask
blue_lower = np.array([94, 80, 2], np.uint8)
blue_upper = np.array([120, 255, 255], np.uint8)
blue_mask = cv2.inRange(hsvFrame, blue_lower, blue_upper)
      
    # Morphological Transform, Dilation
    # for each color and bitwise_and operator
    # between imageFrame and mask determines
    # to detect only that particular color
kernal = np.ones((5, 5), "uint8")
      
    # For red color
red_mask = cv2.dilate(red_mask, kernal)
res_red = cv2.bitwise_and(img, img, mask = red_mask)
      
    # For green color
green_mask = cv2.dilate(green_mask, kernal)
res_green = cv2.bitwise_and(img, img, mask = green_mask)
                                
      
    # For blue color
blue_mask = cv2.dilate(blue_mask, kernal)
res_blue = cv2.bitwise_and(img, img, mask = blue_mask)
                               
for i in contours:
    if c == 0:
        c = 1
        continue

    approx = cv2.approxPolyDP(i, 0.01 * cv2.arcLength(i, True), True)
	
    # using drawContours() function
    cv2.drawContours(img, [i], 0, (0, 0, 255), 5)

    # finding center point of shape
    M = cv2.moments(i)
    if M['m00'] != 0.0:
        x = int(M['m10']/M['m00'])
        y = int(M['m01']/M['m00'])

    # putting shape name at center of each shape
    if len(approx) == 3:
        x='Triangle'

    elif len(approx) == 4:
        x='Quadrilateral'
		
    elif len(approx) == 5:
        x='Pentagon'

    elif len(approx) == 6:
        x='Hexagon'

    else:
        x='Circle'
	
    M = cv2.moments(i)
    if M['m00'] != 0:
        cx = int(M['m10']/M['m00'])
        cy = int(M['m01']/M['m00'])
        print((x,cx,cy))
	
