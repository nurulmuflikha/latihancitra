#konversi citra RGB ke warna HSV

import cv2
import numpy as np

img = cv2.imread('hsl3.png')
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

lower_red = np.array([0, 0, 50])
upper_red = np.array([10, 255, 255])

mask = cv2.inRange(hsv, lower_red, upper_red)

result = cv2.bitwise_and(img, img, mask=mask)
cv2.imshow("Result", result)
cv2.waitKey(0)