import numpy as np, cv2
img = cv2.imread("C:\\Users\\User\\Desktop\\Image\\Book2.jpg")
h, w = img.shape[:2]
draw = img.copy()
pts_cnt = 0
pts = np.zeros((4, 2), dtype=np.float32)

def onMouse(event, x, y, flags, param):  # 마우스 이벤트 콜백 함수 구현

    global pts_cnt  # 마우스로 찍은 좌표의 개수 저장

    if event == cv2.EVENT_LBUTTONDOWN:
        cv2.circle(draw, (x, y), 10, (0, 255, 0), -1)  # 좌표에 초록색 동그라미 표시
        cv2.imshow('scanning', draw)
        pts[pts_cnt] = [x, y]  # 마우스 좌표 저장
        pts_cnt += 1

        if pts_cnt == 4:  # 좌표 4개 수집
            # 좌표 4개 중 상하좌우 찾기
            sm = np.sum(pts, axis=1)  # 4쌍 좌표 각각 x+y 계산
            diff = np.diff(pts, axis=1)  # 4쌍 좌표 각각 x-y 계산
            topLeft = pts[np.argmin(sm)]  # x+y가 가장 작은 값이 좌상단 좌표
            bottomRight = pts[np.argmax(sm)]  # x+y가 가장 큰 값이 우하단 좌표
            topRight = pts[np.argmin(diff)]  # x-y가 가장 작은 값이 우상단 좌표
            bottomLeft = pts[np.argmax(diff)]  # x-y가 가장 큰 값이 좌하단 좌표
            # 변환 전 4개의 좌표
            pts1 = np.array([topLeft, topRight, bottomRight, bottomLeft], dtype=np.float32)
            # 변환 후 4개의 좌표d
            pts2 = np.array([[0, 0], [w-100, 0], [w-100, h-100], [0, h-100]], dtype=np.float32)
            # 변환행렬 계산i
            mtrx = cv2.getPerspectiveTransform(pts1, pts2)
            # 원근 변환 적용
            result = cv2.warpPerspective(img, mtrx, (w-100, h-100))
            cv2.imshow('scanned', result)

cv2.imshow('scanning', img)
cv2.setMouseCallback('scanning', onMouse)
cv2.waitKey(0)
cv2.destroyAllWindows()


