from picamera.array import PiRGBArray
from picamera import PiCamera
import cv2
import numpy as np
import gpiozero
import threading

camera = PiCamera()
image_width = 640
image_height = 480

camera.resolution = (image_width, image_height)
camera.framerate = 32
camera.brightness =63
#rawCapture = PiRGBArray(camera, size=(640,480))
rawCapture = PiRGBArray(camera, size=(image_width, image_height))
center_image_x = image_width / 2
center_image_y = image_height / 2
minimun_area = 250
maximum_area = 100000

robot = gpiozero.Robot(left=(17,28), right=(27,22))
forward_speed = 0.3
turn_speed = 0.5

HUE_VALUE = 85

lower_color = np.array([HUE_VALUE-10, 100, 100])
upper_color = np.array([HUE_VALUE+10, 255, 255])

for frame in camera.capture_continuous(rawCapture, format="bgr", use_video_port=True):
    image = frame.array
    hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    color_mask = cv2.inRange(hsv, lower_color, upper_color)
    contours, hierarchy = cv2.findContours(color_mask, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
     
    object_area = 0
    object_x = 0
    object_y = 0
    cv2.imshow("mask", image)
    cv2.imshow("color_mask", color_mask)
    
    rawCapture.truncate(0)
    k = cv2.waitKey(5)
    if "q" == chr(k & 255):
        break


""""
    for contour in contours:
        x, y, width, height = cv2.boundingRect(contour)
        found_area = width * height
        center_x = x + (width / 2)
        center_y = y + (height / 2)
        
        if object_area < found_area:
            object_area = found_area
            object_x = center_x
            object_y = center_y
    
    if object_area > 0:
        ball_location = [object_area, object_x, object_y]
    else:
        ball_location = None
        
    if ball_location:
        if(ball_location[0] > minimun_area) and (ball_location[0] < maximum_area):
            if ball_location[1] > (center_image_x + (image_width/3)):
                robot.right(turn_speed)
                print("Turning Right")
            elif ball_location[1] < (center_image_x - (image_width/3)):
                robot.left(turn_speed)
                print("Turning Left")
            else:
                robot.forward(forward_speed)
        
        elif (ball_location[0] < minimun_area):
            robot.left(turn_speed)
            print("Target is not larger enough, searching")
        else:
            robot.stop()
            print("Target large enough, stopping")
    else:
        robot.left(turn_speed)
        print("Target not found, searching")
"""
##rawCapture.truncate(0)
    

        
        
    
        
        
