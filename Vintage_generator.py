# -*- coding: utf-8 -*-
"""
Created on Mon Oct  9 18:02:33 2017

Charles Mason
cmmason
Brandon Johnson
bjohnson1

“On my honor, I have not given, nor received, nor witnessed any unauthorized
assistance on this work.”

we used the following outside sources to help create our code
https://docs.opencv.org/3.3.0/da/d6e/tutorial_py_geometric_transformations.html
https://extr3metech.wordpress.com/2012/09/23/convert-photo-to-grayscale-with-python-opencv/
"""

import cv2
import numpy as np
import scipy as sp

#test photo
photo = cv2.imread("Source.jpg")
photo_2 = cv2.imread("Source_2.jpg")

def antiqued(image):

    img = image
    gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    antique_img = cv2.imread("Overlay_1.jpg")
    antique1_img = cv2.imread("Overlay_2.jpg")

    row, col = gray_img.shape
    #resize overlays
    resize1_img = cv2.resize(antique_img, (col, row), interpolation = cv2.INTER_LINEAR)
    resize2_img = cv2.resize(antique1_img, (col, row), interpolation = cv2.INTER_LINEAR)

    new_image = np.zeros( (row, col, 3) , dtype=np.uint8)
    ave = 0
    for r in range(row):
        for c in range(col):
            gray = (gray_img[r][c])*.55
            anti1 = (resize1_img[r][c])*.3
            anti2 = (resize2_img[r][c])*.15
            #average out the overlays with the input image
            ave = gray + anti1 + anti2
            new_image[r][c] = ave

    return new_image

#test code
cv2.imwrite('Output.png',antiqued(photo))
cv2.imwrite('Output_1.png',antiqued(photo_2))

cv2.waitKey(0)
cv2.destroyAllWindows()
