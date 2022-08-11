import cv2

src = cv2.imread("C:\\Users\\User\\Desktop\\Image\\ara.jpg", cv2.IMREAD_COLOR)
height, width, channel = src.shape

dst = cv2.pyrUp(src, dstsize=(width * 2, height * 2), borderType=cv2.BORDER_DEFAULT)
dst2 = cv2.pyrDown(dst)

cv2.imshow("src", src)
cv2.imshow("dst2", dst2)
cv2.waitKey()
cv2.destroyAllWindows()
