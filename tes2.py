import cv2
import numpy as np

# Load gambar
img = cv2.imread('hsl3.png')

# Konversi ke HSV
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

# Tentukan nilai lower dan upper untuk cabai masak
lower_red = np.array([0, 70, 50])
upper_red = np.array([10, 255, 255])

# Thresholding untuk memisahkan cabai masak
mask = cv2.inRange(hsv, lower_red, upper_red)

# Morphological operation untuk menghilangkan noise
kernel = np.ones((5,5),np.uint8)
opening = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel)

# Deteksi kontur
contours, _ = cv2.findContours(opening, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# initialize the count of ripe and unripe peppers
jumlah_cabai_masak = 0
jumlah_cabai_mentah = 0

# Hitung jumlah cabai dan cabai mentah
for contour in contours:
    x,y,w,h = cv2.boundingRect(contour)
    area = cv2.contourArea(contour)
    if area > 2800: # kondisi cabai yang terdeteksi harus lebih besar dari 2800 piksel
        jumlah_cabai_masak += 1
        cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),1) # warna merah untuk cabai masak
    elif area < 1500:
        jumlah_cabai_mentah += 1
        cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),1) # warna hijau untuk cabai mentah

# Print the count of ripe and unripe peppers
print("Jumlah cabai masak: ", jumlah_cabai_masak)
print("Jumlah cabai mentah: ", jumlah_cabai_mentah)

# Tampilkan gambar dengan deteksi cabai dan jumlah objek
cv2.putText(img, "Jumlah cabai masak: " + str(jumlah_cabai_masak), (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)
cv2.putText(img, "Jumlah cabai mentah: " + str(jumlah_cabai_mentah), (50, 80), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)
cv2.imshow("Deteksi Cabai", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
