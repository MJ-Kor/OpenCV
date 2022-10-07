import numpy as np
import cv2

src = cv2.imread("C:\\Users\\User\\Desktop\\Image\\office.jpg")

kernel = cv2.getStructuringElement(cv2.MORPH_CROSS, (9, 9))
dst = cv2.morphologyEx(src, cv2.MORPH_OPEN, kernel, iterations=9)

cv2.imshow('dst', dst)
cv2.waitKey(0)
cv2.destroyAllWindows()

