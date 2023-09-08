import cv2
import numpy as np

#baca gambar
img = cv2.imread('hslcabe.png') 

#konversi RGB ke HSV
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

#Range warna kuning segmentasi/klasifikasi
lower = np.array([20, 100, 100], dtype=np.uint8)
upper = np.array([40, 255, 255], dtype=np.uint8)
mask = cv2.inRange(hsv, lower, upper)
kernel = np.ones((25,25), np.uint8)

#dipertembal piksel objek
dilation = cv2.dilate(mask, kernel, iterations = 1)

#diperkecil supaya tidak berdempet piksel objek
erosion = cv2.erode(mask, kernel, iterations = 1)

contours, hierarchy = cv2.findContours(dilation,cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

resultImg = img.copy()

contour = []

for i in range(len(contours)):
	cnt = contours[i]
	(x,y),radius = cv2.minEnclosingCircle(cnt)
	
	center = (int(x), int(y))
	
	if (int(radius) > 1):
		contour.append(cnt)
	
	resultImg = cv2.circle(resultImg, center, int(radius), (255,0,0), 3)
	
cv2.imshow('image', resultImg)
cv2.waitKey(0)
cv2.destroyAllWindows()
