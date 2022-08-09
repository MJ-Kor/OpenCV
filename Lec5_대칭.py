import cv2

src = cv2.imread("C:\\Users\\User\\Desktop\\Image\\glass.jpg", cv2.IMREAD_COLOR)
dst = cv2.flip(src, 0)
# 대칭 함수 :: cv2.flip(src, flipCode)
# src : 원본 이미지
# flipCode : 대칭 축
# flipCode < 0은 XY(상하좌우) 대칭을 적용
# flipCode = 0은 X(상하) 대칭을 적용
# flipCode > 0은 Y(좌우) 대칭을 적용

cv2.imshow("src", src)
cv2.imshow("dst", dst)
cv2.waitKey()
cv2.destroyAllWindows()

# 대칭은 기하학적 측면에서 반사의 의미를 갖고 이는 2차원 유클리드 공간에서 선형 변환을 진행한다.
# 그람-슈미트과정을 이용 - https://big-dream-world.tistory.com/48