import cv2
import numpy as np

# Load gambar citra
img = cv2.imread('hslcabe.png', cv2.IMREAD_GRAYSCALE)

# Thresholding pada gambar
_, threshold = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)

# Membuat kernel untuk dilated
kernel = np.ones((5,5), np.uint8)

# Melakukan operasi dilated pada gambar
dilated = cv2.dilate(threshold, kernel, iterations=1)

# Menampilkan hasil pengolahan citra
cv2.imshow('Gambar Asli', img)
cv2.imshow('Thresholding', threshold)
cv2.imshow('Dilated', dilated)

cv2.waitKey(0)
cv2.destroyAllWindows()
