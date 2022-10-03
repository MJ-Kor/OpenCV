import numpy as np
import cv2

src = cv2.imread("C:\\Users\\User\\Desktop\\Image\\zebra.jpg")

kernel = cv2.getStructuringElement(cv2.MORPH_CROSS, (9, 9))
dilate = cv2.dilate(src, kernel, anchor=(-1, -1), iterations=5)
erode = cv2.erode(src, kernel, anchor=(-1, -1), iterations=5)

cv2.imshow('src', src)
cv2.imshow('dilate', dilate)
cv2.imshow('erode', erode)
cv2.waitKey(0)
cv2.destroyAllWindows()


