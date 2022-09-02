import cv2

src1 = cv2.imread("C:\\Users\\User\\Desktop\\Image\\geese.jpg")
src2 = cv2.imread("C:\\Users\\User\\Desktop\\Image\\fruits.jpg")
alpha = 0.5
img = cv2.addWeighted(src1, alpha, src2, 1-alpha, 0.0)

cv2.imshow("img", img)
cv2.waitKey()
cv2.destroyAllWindows()

