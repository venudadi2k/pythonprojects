import numpy as np
import cv2

#read the first picture 
first = cv2.imread('img1.png')
first.shape

#read the second picture
second = cv2.imread('img2.png')
second.shape

#display both pictures
cv2.imshow('first',first)
cv2.waitKey()
cv2.destroyAllWindows()

cv2.imshow('second',second)
cv2.waitKey()
cv2.destroyAllWindows()

#cropping the pictures 
crop_first = first[60:700,250:600]
cv2.imshow('crop_first',crop_first)
cv2.waitKey()
cv2.destroyAllWindows()


crop_second = second[60:700,250:600]
cv2.imshow('crop_second',crop_second)
cv2.waitKey()
cv2.destroyAllWindows()

conc = np.concatenate((first,second),axis=0)

hori = np.hstack((first,second))

first = cv2.resize(first,(299,168))

first.shape
second = cv2.resize(second,(299,168))
second.shape
hori = np.hstack((first,second))

cv2.imshow("HORIZONTAL COLLAGE",hori)
cv2.waitKey()
cv2.destroyAllWindows()
