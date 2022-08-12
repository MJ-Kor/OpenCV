import cv2

img = cv2.imread("C:\\Users\\User\\Desktop\\Image\\whitebutterfly.jpg")

x_pos, y_pos, width, height = cv2.selectROI("location", img, True)
# 마우스 클릭 좌표 값 확인 메서드 :: cv2.selectROI(winname, mat, lattice_form)
# winname : 윈도우 창 이름
# mat : 적용 이미지
# lattice_form : 격자 형태

print("x, y :", x_pos, y_pos)
print("width, height :", width, height)

cv2.destroyAllWindows()
