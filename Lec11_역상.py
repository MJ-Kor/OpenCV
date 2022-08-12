import cv2

src = cv2.imread("C:\\Users\\User\\Desktop\\Image\\whitebutterfly.jpg")
dst = cv2.bitwise_not(src)
# Not 연산 함수 :: cv2.bitwise_not(src, mask)
# src : 원본 이미지
# mask : not 연산을 적용할 특정 영역을 의미, 마스크 배열이 포함되어 있다면, 해당 영역만 반전 연산을 적용한다.

cv2.imshow("src", src)
cv2.imshow("dst", dst)
cv2.waitKey()
cv2.destroyAllWindows()