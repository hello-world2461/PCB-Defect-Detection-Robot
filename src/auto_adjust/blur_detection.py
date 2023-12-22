import cv2 as cv
import numpy as np
from skimage import filters

def is_img_blurry(image_path):
    #Read the image as grayscale
    img = cv.imread(image_path, cv.COLOR_BGR2GRAY)

    #Find variance of Sobel gradient
    sobel_variation = filters.sobel(img).var()
    return sobel_variation
