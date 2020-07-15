import numpy as np
import cv2
from detector import detect
from metric import calc_metric

cap = cv2.VideoCapture('test.mp4')

threshold = 0.37

while(cap.isOpened()):
    ret, frame = cap.read()

    boxes = detect(frame)

    for box in boxes:
        img = frame[box[1]:box[3], box[0]:box[2]]

        metric = calc_metric(img)

        cv2.rectangle(frame, (box[0], box[1]), (box[2], box[3]), (232, 35, 244), 2)

        if (metric > threshold):
            cv2.putText(frame, 'mask', (box[0], box[1]), cv2.FONT_HERSHEY_SIMPLEX,  
                   1, (255, 0, 0) , 2, cv2.LINE_AA) 
        else:
            cv2.putText(frame, 'no mask', (box[0], box[1]), cv2.FONT_HERSHEY_SIMPLEX,  
                   1, (255, 0, 0) , 2, cv2.LINE_AA) 

    cv2.imshow('frame',frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()