import cv2
import numpy as np

img = cv2.imread('hslcabe3.png')
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

lower_red = np.array([0, 70, 50])
upper_red = np.array([10, 255, 255])


mask = cv2.inRange(hsv, lower_red, upper_red)
contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# initialize the count of ripe and unripe peppers
jumlah_cabai_masak = 0
jumlah_cabai_mentah = 0

# Hitung jumlah cabai dan cabai mentah
for contour in contours:
    x,y,w,h = cv2.boundingRect(contour)
    area = cv2.contourArea(contour)
    if area > 2800: # kondisi cabai yang terdeteksi harus lebih besar dari 500 piksel
        jumlah_cabai_masak += 1
        cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),1) # warna merah untuk cabai masak
    elif area < 1500:
        jumlah_cabai_mentah += 1
        cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),1) # warna hijau untuk cabai mentah

# Print the count of ripe and unripe peppers
print("Jumlah cabai masak: ", jumlah_cabai_masak)
print("Jumlah cabai mentah: ", jumlah_cabai_mentah)

cv2.imshow("Result", img)
cv2.waitKey(0)