import numpy as np
import os
import cv2
from detector import detect
from color_metric import calc_color_metric
from paint_mask import painting_mask


def detection_masks(threshold):
    data_folder = os.path.join(os.path.dirname(__file__), '..', '..', 'data')
    img_file = os.path.join(data_folder, 'my2_cut.mp4')
    cap = cv2.VideoCapture(img_file)

    # video recording
    fourcc = cv2.VideoWriter_fourcc(*'MP4V')
    out = cv2.VideoWriter('output.mp4',fourcc, 20.0, (1258,720))

    while(cap.isOpened()):
        ret, frame = cap.read()

        with_m = 0
        wihout_m = 0

        boxes = detect(frame)
        for box in boxes:

            img = frame[box[1]:box[3], box[0]:box[2]]
            cv2.rectangle(frame, (box[0], box[1]), (box[2], box[3]), (255, 255, 255), 1)
            ih, iw = img.shape[:-1]

            metric = calc_color_metric(img)
            
            if (metric > threshold):
                with_m += 1
                cv2.putText(frame, 'mask', (box[0], box[1]), cv2.FONT_HERSHEY_SIMPLEX,  
                            0.8, (0, 255, 0) , 2, cv2.LINE_AA) 
            else:
                wihout_m += 1
                cv2.putText(frame, 'no mask', (box[0], box[1]), cv2.FONT_HERSHEY_SIMPLEX,  
                            0.8, (0, 0, 255) , 2, cv2.LINE_AA)
                # painting mask
                # cv2.putText(frame, 'painting', (box[0] - 5, box[1]), cv2.FONT_HERSHEY_SIMPLEX,  
                            # 0.8, (255, 0, 0) , 2, cv2.LINE_AA)
                # frame = painting_mask(frame, box)

        cv2.rectangle(frame, (12, 660), (200, 705), (0,0,0), -1)
        cv2.putText(frame, "with mask: " + str(with_m), (14,680), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 1, cv2.LINE_AA) 
        cv2.putText(frame, "without mask: " + str(wihout_m), (14,700), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 1, cv2.LINE_AA)

        cv2.imshow('frame',frame)
        out.write(frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    out.release()
    cap.release()
    cv2.destroyAllWindows()