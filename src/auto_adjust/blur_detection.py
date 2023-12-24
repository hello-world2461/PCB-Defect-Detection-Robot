import cv2 as cv
import numpy as np
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



def adjust():
    queue_size=2        #Length of queue (compare 2 images)
    threshold = 1000    #Value of 1000+ is clear

    #Initialize a deque to store captured images
    image_queue = deque(maxlen=queue_size)
    
    #Initialize a flag to indicate whether to continue capturing images
    capturing = True

    #Do autofocus until image is not blurry anymore 
    while(capturing):

        # Capture an image (replace this with your actual image capture code)
        image = cv.VideoCapture(0).read()[1]  # Assuming capturing from a webcam

        # Add the new image to the deque
        image_queue.append(image)

        # Compare consecutive pairs of images
        if len(image_queue) == queue_size:
            current_image = image_queue[-1]
            previous_image = image_queue[-2]

            #Checks if previous image is blurrier than current image
            similarity_score = compare_images(previous_image, current_image)

        #Stop "while" loop once camera is focus is greater than threshold val
        if (is_img_blurry(current_image) > threshold):
            capturing = False


def compare_images(img1, img2):
    pass
#    if (is_img_blurry(img1) > is_img_blurry(img2)):

    #TAKE IMAGE 1
    #MOVE CAMERA 1-2 ROTATIONS UP
    #TAKE IMAGE 2
    #IDENTIFY IF IMG 1 OR IMG 2 IS MORE BLURRY
    #IF IMG1 MORE BLURRY, MOVE CAMERA UP HALF ROTATION
    #DEPEDNING ON HOW CLOSE IT IS TO THRESHOLD CHANGE INCREMENTS OF THRESHOLD 





test_img = "data\\blurry_images_test\\WIN_20231223_16_30_49_Pro.jpg"
is_img_blurry(test_img)