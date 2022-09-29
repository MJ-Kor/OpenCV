import cv2
src1 = cv2.imread("C:\\Users\\User\\Desktop\\Image\\poly.png")
src2 = cv2.imread("C:\\Users\\User\\Desktop\\Image\\poly.png")
gray = cv2.cvtColor(src1, cv2.COLOR_RGB2GRAY)

ret, binary = cv2.threshold(gray, 0, 255, cv2.THRESH_OTSU)

contours, hierarchy = cv2.findContours(binary, cv2.RETR_LIST, cv2.CHAIN_APPROX_TC89_KCOS)

for contour in contours:
    epsilon1 = cv2.arcLength(contour, True) * 0.1
    epsilon2 = cv2.arcLength(contour, True) * 0.02
    approx_poly1 = cv2.approxPolyDP(contour, epsilon1, True)
    approx_poly2 = cv2.approxPolyDP(contour, epsilon2, True)

    for approx in approx_poly1:
        cv2.circle(src1, tuple(approx[0]), 10, (255, 0, 0), -1)
    for approx in approx_poly2:
        cv2.circle(src2, tuple(approx[0]), 10, (255, 0, 0), -1)

cv2.drawContours(src1, [approx_poly1], 0, (0, 0, 255), 2)
cv2.drawContours(src2, [approx_poly2], 0, (0, 0, 255), 2)
cv2.imshow("src1", src1)
cv2.imshow("src2", src2)
cv2.waitKey(0)
cv2.destroyAllWindows()

