import cv2
import numpy as np

img = cv2.imread('images/flower_input.jpg')
img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

result = np.zeros(img.shape)

rows, cols = img.shape

for i in range(14, rows-14):
    for j in range(14, cols-14):
        if img[i, j] < 160:
            small_img = img[i-14:i+15, j-14:j+15]
            small_img_1d = small_img.reshape(841)
            small_img_1d_sorted = np.sort(small_img_1d)
            result[i, j] = small_img_1d_sorted[420]
        else:
            result[i, j] = img[i, j]

cv2.imwrite('output_1.jpg', result)