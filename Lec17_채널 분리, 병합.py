import cv2
src = cv2.imread("C:\\Users\\User\\Desktop\\Image\\food.jpg")
b, g, r = cv2.split(src)
inverse = cv2.merge([r,g,b])
cv2.imshow("b", b)
cv2.imshow("g", g)
cv2.imshow("r", r)
print(src[0,:5,:])
print(inverse[0,:5,:])
cv2.imshow("src", src)
cv2.imshow("inverse", inverse)
cv2.waitKey()
cv2.destroyAllWindows()
