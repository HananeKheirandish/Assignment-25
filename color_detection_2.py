import cv2
import numpy as np

vedio_cap = cv2.VideoCapture(0)

while True:
    ret, frame = vedio_cap.read()

    if ret == False:
        break

    frame = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)     
    frame = cv2.resize(frame, (500, 500))

    cv2.rectangle(frame,(180,170), (320,310), (0, 0, 0), 4)

    mask = np.ones((29, 29)) / 841

    blur_frame = cv2.filter2D(frame, -1, mask)
    blur_frame[170:310, 180:320] = cv2.equalizeHist(frame[170:310, 180:320])
    color_detection = blur_frame[170:310, 180:320]

    color = ''
    if np.average(color_detection) <= 80:
        color = 'Black'
    elif 80 < np.average(color_detection) <= 120:
        color = 'Gray'
    else:
        color = 'White'

    cv2.putText(blur_frame, color, (20, 50), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 0, 0), 2)

    cv2.imshow('output', blur_frame)
    cv2.waitKey(1)