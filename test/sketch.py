import numpy as np
import cv2
import imageio
import scipy.ndimage

img = 'img/example4.jpg'

def greyscale(rgb):
    return np.dot(rgb[...,:3],[0.299,0.587,0.114])

def dodge(front,back):
    result=front*230/(255-back)
    result[result>255]=255
    result[back==255]=255
    return result.astype('uint8')

i = imageio.imread(img)

g = greyscale(i)

s = 255-g

b = scipy.ndimage.filters.gaussian_filter(s,sigma=10)

r = dodge(b,g)

cv2.imwrite('img/sketch4.png', r)