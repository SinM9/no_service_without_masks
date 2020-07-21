import os
import cv2
import numpy as np
from PIL import Image
from detector import detect
from landmarks import landmarks_35

data_folder = os.path.join(os.path.dirname(__file__), '..', '..', 'data')
image = os.path.join(data_folder,'no_mask2.jpg')
img = cv2.imread(image)
image2 = os.path.join(data_folder,'medical-mask2.png')
img2 = cv2.imread(image2)
boxes=detect(data_folder, image)
for box in boxes:
    img1 = img[box[1]:box[3],box[0]:box[2]]
    x,y = landmarks_35(img1)
    ih, iw = img1.shape[:-1]
    roi = img1[y[19]:ih, 0:iw]
    img2 = cv2.resize(img2, (iw, ih - y[19]))
    img2gray = cv2.cvtColor(img2,cv2.COLOR_BGR2GRAY)
    ret, mask = cv2.threshold(img2gray, 10, 255, cv2.THRESH_BINARY)
    mask_inv = cv2.bitwise_not(mask)

    img1_bg = cv2.bitwise_and(roi, roi, mask = mask_inv)
    img2_fg = cv2.bitwise_and(img2, img2, mask = mask)

    dst = cv2.add(img1_bg, img2_fg)
    img1[y[19]:ih, 0:iw] = dst
    img[boxes[0][1] + y[19]:boxes[0][3], boxes[0][0]:boxes[0][2]] = dst

cv2.imwrite('res.jpg',img)


