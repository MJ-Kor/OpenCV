import cv2
import numpy as np

src = cv2.imread("C:\\Users\\User\\Desktop\\Image\\harvest.jpg")
height, width, channel = src.shape
print(height, width, channel)

srcPoint = np.array([[500, 200], [1200, 200], [width, height], [0, height]], dtype=np.float32)
dstPoint = np.array([[0, 0], [width, 0], [width, height], [0, height]], dtype=np.float32)

matrix = cv2.getPerspectiveTransform(srcPoint, dstPoint)
dst = cv2.warpPerspective(src, matrix, (width, height))

cv2.imshow("dst", dst)
cv2.imshow("src", src)
cv2.waitKey()
cv2.destroyAllWindows()

