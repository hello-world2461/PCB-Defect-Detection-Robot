import cv2 as cv
import numpy as np
import time
from skimage import filters
from collections import deque

#Function returns blur coefficient
def is_img_blurry(image_path):
    img = cv.imread(image_path, cv.COLOR_BGR2GRAY)

    #Apply the Sobel filter to detect edges
    sobelx = cv.Sobel(img, cv.CV_64F, 1, 0, ksize=5)
    sobely = cv.Sobel(img, cv.CV_64F, 0, 1, ksize=5)

    #Calculate the gradient magnitude
    gradient_magnitude = np.sqrt(sobelx**2 + sobely**2)

    #Calculate the mean gradient magnitude (higher --> not blurry)
    mean_gradient = np.mean(gradient_magnitude)
    print (mean_gradient)
    return mean_gradient #Value of 1000> is focused

#Algorithm to focus camera
def focus_camera(direction_of_motor, rotation_factor, threshold):
    #Define which camera you want to use (webcame = 0)
    cam_port = 0
    cam = cv.VideoCapture(cam_port) 
  
    #Read input of camera
    _, previous_image = cam.read()

    #Change height of camera (NEED TO FILL IN WHEN I GET TO STEPPER MOTOR CONTROLS)
    #move_motor(direction_of_motor, rotation_factor)

    #Add a 1 sec delay so there are no vibrations from the stepper motor
    time.sleep(1)

    #Read camera input after heigh adjustment
    _, current_image = cam.read()

    #Find how much to rotate motor by
    rotatation_factor = ((threshold - is_img_blurry(current_image))/100)

    #If rotation factor is too low we exit the recursive function (8th of a turn)
    if (rotatation_factor <= 0.125): 
        print("Camera is in focus.")
        return

    #Compare focus of images
    if (is_img_blurry(previous_image) > is_img_blurry(current_image)):
        #Change direction of motor & how much to rotate by
        direction_of_motor = -1
        #move_motor(direction_of_motor, rotation_factor)
        focus_camera(direction_of_motor, rotation_factor)
    
    elif (is_img_blurry(previous_image) < is_img_blurry(current_image)):
        #Change direction of motor & how much to rotate by (OPPOSITE DIRECTION)
        direction_of_motor = 1
        #move_motor(direction_of_motor, rotation_factor)
        focus_camera(direction_of_motor, rotation_factor)

    #If blur value does not change, this means the camera height has not changed. 
    elif (is_img_blurry(previous_image) == is_img_blurry(current_image)):
        raise ValueError("No change in blur value, camera has not moved. Check if hardware is working.")


test_img = "data\\blurry_images_test\\WIN_20231223_16_30_49_Pro.jpg"
is_img_blurry(test_img)

#focus_camera(-1, 200, 1000)
