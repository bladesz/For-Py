#Import all libraries we will use
import random
import numpy as np
import cv2

#let's create a 6 x 6 matrix with all pixels in black color
img = np.zeros((6,6,3),np.uint8)

#let's use "for" cycle to change colorspace of pixel in a random way
for x in range(6):
    for y in range(6):
        #We use "0" for black color (do nothing) and "1" for white color (change pixel value to [255,255,255])
        value = random.randint(0,1)
        if value == 1:
            img[x,y] = [255,255,255]

#save our image as a "png" image
cv2.imwrite("6_x_6.png",img)
