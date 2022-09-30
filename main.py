import cv2
import cv2.aruco as aruco
import numpy as np
import os
from PIL import Image, ImageDraw, ImageFilter

#############################################################################################################################
#find aruco

def find_ar(img,markerSize=6,totalMarkers = 250,draw=True):
    
    global x_centerPixel,y_centerPixel,ids
    
    imgGray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    key = getattr(aruco, f'DICT_{markerSize}X{markerSize}_{totalMarkers}')
    arucoDict = aruco.Dictionary_get(key)
    arucoParameters = aruco.DetectorParameters_create()
    corner , ids ,rejected = aruco.detectMarkers(imgGray,arucoDict,parameters=arucoParameters)
    if draw:
        img = aruco.drawDetectedMarkers(img,corner)
        
    x_sum = corner[0][0][0][0]+ corner[0][0][1][0]+ corner[0][0][2][0]+ corner[0][0][3][0]
    y_sum = corner[0][0][0][1]+ corner[0][0][1][1]+ corner[0][0][2][1]+ corner[0][0][3][1]
    
    x_centerPixel = x_sum*0.25
    y_centerPixel = y_sum*0.25
    
    
    print("ar-center:","x =",x_centerPixel,"|","y =",y_centerPixel)
    #print(corner)
    for line in corner:
        print ('  '.join(map(str, line)))
    #print("box= ",corner)
    print("id= ",ids)
    #print("rejected= ",rejected)
    
    return corner,ids,x_centerPixel,y_centerPixel

"""def augmentAruco(corner,ids,img,imgAug,draw=True):
    
    tl = corner[0][0][0],corner[0][0][1]
    tr = corner[0][1][0],corner[0][1][1]
    br = corner[0][2][0],corner[0][2][1]
    bl = corner[0][3][0],corner[0][3][1]
    
    h,w,c =imgAug.shape
    
    pts1 = np.array([tl,tr,br,bl])
    pts2 = np.float32([[0,0],[w,0],[w,h],[0,h]])
    matrix = cv2.findHomography(pts1,pts2)
    imgOut = cv2.warpPerspective(imgAug,matrix,(img.shape[1],img.shape[0]))
    cv2.fillConvexPoly(img,pts1.astype(int),(0,0,0))
    #imgOut = img + imgOut
    
    return imgOut"""

    

def main():
    img = cv2.imread("test.jpg")
    #imgAug = cv2.imread("LOGO/1.jpg")
    find_ar(img)
    """if len(ArucoFound[0])!=0:
        for corner,ids in zip(ArucoFound[0],ArucoFound[1]):"""
            
            
            
            
    #resize= cv2.resize(img,(500,500))
    #cv2.imshow("img", resize)
    #cv2.waitKey(0)
    #cv2.destroyAllWindows()


if __name__ =='__main__':
    main()

#############################################################################################################################

#place IMG by pillow

imgmain = Image.open("test.jpg")
imgplace = Image.open("LOGO/1.jpg")
imgplaceSize = imgplace.size
backimg =imgmain.copy()
backimg.paste(imgplace,(int(x_centerPixel)-int(imgplaceSize[0]/2),int(y_centerPixel)-int(imgplaceSize[1]/2)))
backimg.save("img_save/testplace.jpg")
#print(imgplace.size)
backimg.show()