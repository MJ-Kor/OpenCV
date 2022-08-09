# 선형 변환 중 하나이며, 회전 변환 행렬을 통해 변환이 진행된다.
# 회전 변환 행렬은 임의의 점을 중심으로 물체를 회전시킨다.
# 회전 변환 행렬의 일부는 반사 행렬과 같은 값을 지닐 수 있다.
# 1. 좌표 값을 회전시키는 회전 행렬 - 원점 중심으로 좌표 값을 회전시켜 매핑
# 2. 좌표 축을 회전시키는 회전 행렬 - 원점을 중심으로 행렬 자체를 회전시켜 새로운 행렬 값 구함
# OpenCV의 회전 함수는 좌표 축 회전 이동 행렬과 동일하다.

import cv2

src = cv2.imread("C:\\Users\\User\\Desktop\\Image\\ara.jpg", cv2.IMREAD_COLOR)

height, width, channel = src.shape
matrix = cv2.getRotationMatrix2D((width/2, height/2), 90, 1)
# 2X3 회전 행렬 생성 함수 :: cv2.getRotationMatrix2D(center, angle, scale)
# center : 튜플 형태로 사용되며 회전의 기준점 의미
# angle : 중심점을 기준으로 회전할 각도
# scale : 이미지 확대 및 축소 비율

dst = cv2.warpAffine(src, matrix, (width, height))
# 아핀 변환 함수 :: cv2.warpAffine(src, M, dsize)
# src : 원본 이미지
# M : 아핀 맵 행렬(회전 행렬)
# dsize : 튜플 형태로 사용되며 출력 이미지의 너비와 높이 의미
# 아핀 공간 : 유클리드 공간의 아핀 기하학적 성질들을 일반화해서 만들어지는 구조이다. 아핀 공간에서는 점에서 점을 빼서 벡터를 얻거나 점에 벡터를 더해 다른 점을 얻을 수는 있지만 원점이 없으므로 점과 점을 더할 수는 없다. 원점이 없음

cv2.imshow("src", src)
cv2.imshow("dst", dst)
cv2.waitKey()
cv2.destroyAllWindows()