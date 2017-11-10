import cv2
import numpy as np
import matplotlib as plt
import il_funcs as il

path1 = 'C:\\Users\\bigse\\Limpiador\\Fotos\\IMG_6079.jpg'
template = 'C:\\Users\\bigse\\Limpiador\\Fotos\\res_6079.jpg'
res_fac = 8

img = cv2.imread(path1)
img = cv2.resize(img, None, fx=(1/res_fac), fy=(1/res_fac), interpolation = cv2.INTER_AREA)
template = cv2.imread(template, 0)
w, h = template.shape[::-1]

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

retval, threshold = cv2.threshold(gray, 75, 255, cv2.THRESH_BINARY)

res = cv2.matchTemplate(gray, template, cv2.TM_CCOEFF_NORMED)
threshold = 0.83
loc = np.where( res >= threshold)

for pt in zip(*loc[::-1]):
    cv2.rectangle(img, pt, (pt[0] + w, pt[1] + h), (0,255,255), 4)
    
cv2.imshow('Detectado', img)

'''
cv2.imshow('75', threshold)
cv2.namedWindow('75', cv2.WINDOW_NORMAL)
'''

cv2.resizeWindow
cv2.waitKey(0)
cv2.destroyAllWindows()