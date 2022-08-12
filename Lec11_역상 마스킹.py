import cv2
import numpy as np

src = cv2.imread("C:\\Users\\User\\Desktop\\Image\\whitebutterfly.jpg")
blank = np.zeros(src.shape[:2], dtype="uint8")
# 0으로만 채워진 array를 생성하는 메서드 :: np.zeros(N_dimensional_array, dtype)
# N_dimensional_array : 0으로 채울 배열의 차원, (2, 3)와 같은 튜플 형태를 입력하면 2행 3열의 2차원 array를 뜻한다.
# dtype : data type, 지정해주지 않을 경우 0.와 같이 소수점이 붙지만 int로 지정해주면 소수점이 사라진다.

mask = cv2.rectangle(blank, (375, 230), (420, 340), (255, 255, 255), -1)
# 사각형 그리는 메서드 :: cv2.rectangle(img, upper_left, bottom_right, borderColor, borderThickness)
# img : 사각형을 넣을 이미지
# upper_left : 사각형 좌측상단 좌표
# bottom_right : 사각형 우측하단 좌표
# borderColor : 테두리선 색상, RGB 코드
# borderThickness : 테두리선 두께, -1로 설정할 경우 채워진 사각형이 그려짐

dst = cv2.bitwise_not(src, mask=mask)
# Not 연산 함수 :: cv2.bitwise_not(src, mask)
# src : 원본 이미지
# mask : not 연산을 적용할 특정 영역을 의미, 마스크 배열이 포함되어 있다면, 해당 영역만 반전 연산을 적용한다.

print(src.shape[:2])
print(np.zeros(src.shape[:2], dtype="uint8"))
cv2.imshow("mask", mask)
cv2.waitKey()
cv2.destroyAllWindows()