import cv2

# Load gambar
img = cv2.imread('cabe2.jpg')

# Mengambil ukuran gambar
height, width, _ = img.shape

# Memperkecil gambar menjadi setengah ukuran aslinya
scale_percent = 20 # persentase yang diinginkan
new_width = int(width * scale_percent / 100)
new_height = int(height * scale_percent / 100)
dim = (new_width, new_height)
resized = cv2.resize(img, dim, interpolation = cv2.INTER_AREA)

# Tampilkan gambar hasil perubahan ukuran
cv2.imshow('Gambar Hasil Perubahan Ukuran', resized)
cv2.waitKey(0)
cv2.destroyAllWindows()