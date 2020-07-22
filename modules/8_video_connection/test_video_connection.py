import os
import numpy as np
import cv2
from detector import detect
from metric import calc_metric

data_folder = os.path.join(os.path.dirname(__file__), '..', '..', 'data')
video_file=os.path.join(data_folder,'my2_cut.mp4')
cap = cv2.VideoCapture(video_file)

threshold = 0.37

while(cap.isOpened()):
    ret, frame = cap.read()
    boxes = detect(frame)
    with_m = 0
    wihout_m = 0

    for box in boxes:
        img = frame[box[1]:box[3], box[0]:box[2]]

        metric = calc_metric(img)

        cv2.rectangle(frame, (box[0], box[1]), (box[2], box[3]), (232, 35, 244), 2)

        if (metric > threshold):
            cv2.putText(frame, 'mask', (box[0], box[1]), cv2.FONT_HERSHEY_SIMPLEX,  
                   1, (0, 255, 0) , 2, cv2.LINE_AA) 
            with_m += 1
        else:
            cv2.putText(frame, 'no mask', (box[0], box[1]), cv2.FONT_HERSHEY_SIMPLEX,  
                   1, (0, 0, 255) , 2, cv2.LINE_AA) 
            wihout_m += 1

    cv2.rectangle(frame, (12, 660), (200, 705), (0,0,0), -1)
    cv2.putText(frame, "with mask: " + str(with_m), (14,680), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 1, cv2.LINE_AA) 
    cv2.putText(frame, "without mask: " + str(wihout_m), (14,700), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 1, cv2.LINE_AA)
    
    cv2.imshow('frame',frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
