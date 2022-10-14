import cv2
src = cv2.imread("C:\\Users\\User\\Desktop\\Image\\apple.jpg")
gray = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)
gray_Gauss = cv2.GaussianBlur(gray, (7,7), 3)
laplacian = cv2.Laplacian(gray, cv2.CV_8U, ksize=5)
laplacian2 = cv2.Laplacian(gray_Gauss, cv2.CV_8U, ksize=5, scale=1)

cv2.imshow("laplacian", laplacian)
cv2.imshow("laplacian2", laplacian2)
cv2.waitKey()
cv2.destroyAllWindows()

