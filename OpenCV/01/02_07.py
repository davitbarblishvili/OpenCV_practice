import numpy as np
import cv2

img = cv2.imread("players.jpg",1)

#scaling
image_half = cv2.resize(img, (0,0), fx = 0.5, fy = 0.5)
image_stretch = cv2.resize(img, (600,600))
image_stretch_near = cv2.resize(img, (600,600), interpolation=cv2.INTER_NEAREST)

cv2.imshow("Half", image_half)
cv2.imshow("stretch", image_stretch)
cv2.imshow("nearest", image_stretch_near)

#rotate
M = cv2.getRotationMatrix2D((0,0), -60, 1)
rotated = cv2.warpAffine(img, M, (img.shape[1], img.shape[0]))
cv2.imshow("rotated", rotated)

cv2.waitKey(0)
cv2.destroyAllWindows()