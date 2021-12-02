import cv2
import numpy as np

img = cv2.imread('images/img_4.jpg')
img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

def convolution(s):
    result = np.zeros(img.shape)

    mask = np.ones((s, s)) / s ** 2

    rows, cols = img.shape

    for i in range(s//2, rows-s//2):
        for j in range(s//2, cols-s//2):
            small_img = img[i-s//2:i+s//2+1, j-s//2:j+s//2+1]
            result[i, j] = np.sum(small_img * mask)
    
    return result

list_size = [3, 5, 7, 15]
i = 0

for size in list_size:
    res = convolution(size)
    cv2.imwrite(f'output4_{i}.jpg', res)
    i += 1