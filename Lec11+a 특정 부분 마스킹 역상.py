import cv2
import numpy as np

src = cv2.imread("C:\\Users\\User\\Desktop\\Image\\whitebutterfly.jpg")

# 영역 좌측 상단 지정
upper_left_x_pos, upper_left_y_pos, width, height = cv2.selectROI("location", src, False)
print("x, y :", upper_left_x_pos, upper_left_y_pos)
print("width, height :", width, height)

# 영역 우측 하단 좌표
bottom_right_x_pos = upper_left_x_pos + width
bottom_right_y_pos = upper_left_y_pos + height

# 원본 이미지와 같은 형식의 배열 생성
blank = np.zeros(src.shape[:2], dtype="uint8")

# 마스킹 영역 지정
mask = cv2.rectangle(blank, (upper_left_x_pos, upper_left_y_pos), (bottom_right_x_pos, bottom_right_y_pos), (255, 255, 255), -1)

# 이미지 역상
dst = cv2.bitwise_not(src, mask=mask)

cv2.imshow("dst", dst)
cv2.waitKey()
cv2.destroyAllWindows()
