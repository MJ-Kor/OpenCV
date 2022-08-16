import cv2

src = cv2.imread("C:\\Users\\User\\Desktop\\Image\\fruits.jpg")
dst = cv2.blur(src,(9, 9), anchor=(-1, -1), borderType=cv2.BORDER_DEFAULT)
# 단순 흐림 효과 함수 :: cv2.blur(src, ksize, anchor, borderType)
# src : 원본 이미지
# ksize : 커널 크기
# anchor : 고정점
# borderType : 테두리 외삽법
# 커널 : 이미지에서 (x, y)의 픽셀과 해당 픽셀 주변을 포함한 작은 크기의 공간
# 커널은 특정한 수식이나 함수 등을 적용해 새로운 이미지를 얻는 알고리즘에서 사용된다.
# 고정점 : 커널을 통해 컨벌루션된 값을 할당한 지점
# 컨벌루션 : 새로운 픽셀을 만들어 내기 위해 커널 크기의 화소 값을 이용해 어떤 시스템을 통과해 계산하는 것

cv2.imshow("dst", dst)
cv2.waitKey()
cv2.destroyAllWindows()