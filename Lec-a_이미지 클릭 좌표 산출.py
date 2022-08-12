import cv2

img = cv2.imread("C:\\Users\\User\\Desktop\\Image\\whitebutterfly.jpg")

x_pos, y_pos, width, height = cv2.selectROI("location", img, False)
print("x, y :", x_pos, y_pos)
print("width, height :", width, height)

cv2.destroyAllWindows()
