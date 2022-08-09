# 특정 영역을 잘라내는 것 : 이미지 상의 관심 영역(Region Of Interest, ROI)
# 이미지를 처리할 때 객체를 탐지하거나 검출하는 영역

import cv2

src = cv2.imread("C:\\Users\\User\\Desktop\\Image\\apple.jpg", cv2.IMREAD_COLOR)
# dst = src[100:600, 200:700].copy()
# # OpenCV의 이미지는 numpy 배열 형식과 동일
# # src 이미지에 src[높이(행), 너비(열)]로 관심 영역을 설정한다.
# # 리스트나 배열의 특정 영역을 자르는 방식과 동일하다.
# # 이미지를 자르거나 복사할 때, dst = src의 형태로 사용하면 얕은 복사가 되어 원본도 영향을 받게되므로 .copy()를 사용해 깊은 복사를 한다.

dst = src.copy()
roi = src[100:600, 200:700]
dst[0:500, 0:500] = roi
# 붙여넣기, 잘라낸 이미지와 붙여넣을 이미지의 크기가 다르다면 이미지를 붙여넣을 수 없다.
cv2.imshow("src", src)
cv2.imshow("dst", dst)
cv2.waitKey()
cv2.destroyAllWindows()