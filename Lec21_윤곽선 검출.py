import cv2

src = cv2.imread("C:\\Users\\User\\Desktop\\Image\\contours.jpg")
gray = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)
ret, binary = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)
binary = cv2.bitwise_not(binary)

contours, hierarchy = cv2.findContours(binary, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)

for i in range(len(contours)):
    cv2.drawContours(src, [contours[i]], 0, (0, 0, 255), 2)
    cv2.putText(src, str(i), tuple(contours[i][0][0]), cv2.FONT_HERSHEY_COMPLEX, 0.8, (0, 200, 0), 1)
    print(i, hierarchy[0][i])
    cv2.imshow("src", src)

print(hierarchy)
cv2.waitKey(0)
cv2.destroyAllWindows()

