
from cv2 import bitwise_and
import matplotlib.pyplot as plt
import cv2
import numpy as np

#Task 1: masking the image region of interest
#function to mask every other thing than the region of image of interst
def region_of_interest(img,vertices):
    #blank matrix that matches image h,w
    mask=np.zeros_like(img)
    
    #retreive the color channel count
    channel_count=img.shape[2]

    #create a match color with the same color channel count
    match_mask_color=(255,) * channel_count

    #fill inside the ploygone other than region of interest with created mask color
    cv2.fillPoly(mask,vertices,match_mask_color)
    
    #image only where above created mask pixel matches
    masked_img=cv2.bitwise_and(img,mask)
    
    return masked_img

# Load an image
image=cv2.imread('lane_line.jpg')

#convert image into RGB format to plot on matplotlib
image=cv2.cvtColor(image,cv2.COLOR_BGR2RGB)

# Find out height and width of image
print(image.shape)#height,width channel
height=image.shape[0]
width=image.shape[1]

#Verices of region of interest ie; triangle shape from midpoint of image
region_of_interest_vertices=[(0,height),(width/2,height/2),(width,height)]

croped_Img=region_of_interest(image,
np.array([region_of_interest_vertices],np.int64),)

#######Masking of Image Ends######

plt.imshow(croped_Img)
plt.show()
