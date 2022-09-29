import cv2
import numpy as np

src = cv2.imread("C:\\Users\\User\\Desktop\\Image\\coffee.jpg")
dst = src.copy()

gray = cv2.cvtColor(src, cv2.COLOR_RGB2GRAY)
corners = cv2.goodFeaturesToTrack(gray, 100, 0.01, 5, blockSize=3, useHarrisDetector=True, k=0.03)

corners = np.array(corners, dtype=np.uint64)

for i in corners:
    cv2.circle(dst, tuple(i[0]), 3, (0, 0, 255), 2)

cv2.imshow("dst", dst)
cv2.waitKey(0)
cv2.destroyAllWindows()

