#coding=utf-8
"""
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#
# fileName : filename.py
# comment  : comment here
# version  : 1.0
# author   : zhengshoujian
# date     : xxxx-xx-xx
#
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
"""
import cv2

def mask(img,img1):
   height,width, c = img1.shape
   for c in range(c):
     for i in range(0, height):
        for j in range(0, width):
           if(img[i,j] >90):
            #print im1[i,j]
            img1[i,j,1] = 100+img1[i,j,1]
			
   cv2.imwrite("leftImg8bit.png",img1)
   return img1
 
 
 
im = cv2.imread("pred.png",cv2.IMREAD_GRAYSCALE)
im1 = cv2.imread("orig.png")




if __name__ == '__main__':
    mask(im,im1)