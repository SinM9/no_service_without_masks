import os
import cv2
import numpy as np
from landmarks import landmarks_35

def painting_mask(image, box):
    data_folder = os.path.join(os.path.dirname(__file__), '..', '..', 'data')
    img_file = os.path.join(data_folder, 'medical-mask3.png')
    img2 = cv2.imread(img_file)
    img1 = image[box[1]:box[3], box[0]:box[2]]
    x,y = landmarks_35(img1)
    ih, iw = img1.shape[:-1]
    roi = img1[y[19]:ih, 0:iw]
    img2 = cv2.resize(img2, (iw, ih - y[19]))
    img2gray = cv2.cvtColor(img2,cv2.COLOR_BGR2GRAY)
    ret, mask = cv2.threshold(img2gray, 10, 255, cv2.THRESH_BINARY)
    mask_inv = cv2.bitwise_not(mask)

    img1_bg = cv2.bitwise_and(roi,roi,mask = mask_inv)
    img2_fg = cv2.bitwise_and(img2,img2,mask = mask)

    dst = cv2.add(img1_bg,img2_fg)
    image[box[1] + y[19]:box[3],box[0]:box[2]] = dst
    ih, iw = img2.shape[:-1]
    image[box[1] + y[19] + int(ih / 3):box[3] - int(ih / 4),box[0]:box[2]] = img2[int(ih / 3): ih - int(ih / 4), 0:iw]
    return image