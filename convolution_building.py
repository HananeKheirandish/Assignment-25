import cv2
import numpy as np

img = cv2.imread('images/building.tif')
img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

result_1 = np.zeros(img.shape)
result_2 = np.zeros(img.shape)

mask_1 = np.array([[-1, 0, 1], 
                [-1, 0, 1],
                [-1, 0, 1]])

mask_2 = np.array([[-1, -1, -1], 
                [0, 0, 0],
                [1, 1, 1]])

rows, cols = img.shape

for i in range(1, rows-1):
    for j in range(1, cols-1):
        small_img = img[i-1:i+2, j-1:j+2]
        result_1[i, j] = np.sum(small_img * mask_1)
        result_2[i, j] = np.sum(small_img * mask_2)

cv2.imwrite('output_3A.jpg', result_1)
cv2.imwrite('output_3B.jpg', result_2)