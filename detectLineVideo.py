import matplotlib.pyplot as plt
import cv2
import numpy as np


def region_of_interest(img,vertices):
    mask=np.zeros_like(img)
    #channel_count=img.shape[2]
    #there is no need  of color channel now the image is in grayscale;in one color

    match_mask_color=(255)

    cv2.fillPoly(mask,vertices,match_mask_color)
    
    masked_img=cv2.bitwise_and(img,mask)
    
    return masked_img

#draw the line
def draw_the_lines(img,lines):
    print(lines)
    img=np.copy(img)
    #blank image of same dimensions
    blank_image=np.zeros((img.shape[0],img.shape[1],3),dtype=np.uint8)
    for line in lines :
        #line is four coordinates of first point and second point of line
        for x1,y1,x2,y2 in line :
            cv2.line(blank_image,(x1,y1),(x2,y2),(255,190,0),thickness=10)


    img=cv2.addWeighted(img,0.8,blank_image,1,0.0)#merge two images with weight  .8 is weight, 1 is beta and 0.0 is gamma
    return img

#image=cv2.imread('lane_line.jpg')
#image=cv2.cvtColor(image,cv2.COLOR_BGR2RGB)

# Find out height and width of image
def process(image):
    height=image.shape[0]
    width=image.shape[1]

    #Verices of region of interest ie; triangle shape from midpoint of image
    region_of_interest_vertices=[(0,height),(width/2,height/2),(width,height)]

    #Task 2: To find out the edges on road

    #Converting image into grayscale
    gray_image=cv2.cvtColor(image,cv2.COLOR_RGB2GRAY)

    #Canny is algorithm to find out edges of any object in image 
    edge_image=cv2.Canny(gray_image,100,120)

    #after converting in gray sclae and finding the edges have to crop
    croped_Img=region_of_interest(edge_image,
    np.array([region_of_interest_vertices],np.int32),)

    #draw lines on the edges we got
    #Hough Transform is a method that is used in image processing to detect
    #  any shape, if that shape can be represented in mathematical form 
    #It can detect the shape even if it is broken or distorted a little bit.

    lines=cv2.HoughLinesP(croped_Img,
    rho=2,
    theta=np.pi/180,
    threshold=50,
    lines=np.array([]),
    minLineLength=40,
    maxLineGap=100)

    image_lines=draw_the_lines(image,lines)
    return image_lines

capture=cv2.VideoCapture('lane_line.mp4')

if( capture.isOpened()==False):
    print("Something Wrong in Loading !")

while(capture.isOpened()):
    ret,frame=capture.read() 
    frame=process(frame)
    cv2.imshow('Road Lanes Detection', frame)
    if(cv2.waitKey(1)) & 0xFF ==ord('q'):
        break

capture.release()
cv2.destroyAllWindows()
