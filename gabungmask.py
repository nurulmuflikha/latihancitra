import cv2
import numpy as np

# load gambar
img = cv2.imread('hsl3.png')

# buat dua mask (contoh)
mask1 = np.zeros(img.shape[:2], np.uint8)
mask2 = np.zeros(img.shape[:2], np.uint8)

mask1[100:400, 200:500] = 255 # set mask 1 pada area tertentu
mask2[300:500, 100:300] = 255 # set mask 2 pada area tertentu

# gabungkan kedua mask
mask_combined = cv2.bitwise_and(mask1, mask2)

# apply mask pada gambar
img_masked = cv2.bitwise_and(img, img, mask=mask_combined)

# hitung nilai rata-rata RGB pada area yang ter-mask
mean_color = cv2.mean(img_masked, mask=mask_combined)

print("Nilai RGB dari gabungan masking 1 dan 2: ", mean_color[:3])

cv2.imshow('img',img)
cv2.imshow('mask1',mask1)
cv2.imshow('mask2',mask2)
cv2.imshow ('mask',mask_combined)
cv2.imshow('img masked', img_masked)
cv2.imshow('mean color', mean_color)
cv2.waitKey(0)

