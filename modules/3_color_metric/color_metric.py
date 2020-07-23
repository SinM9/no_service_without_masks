import cv2
import numpy as np
import math

def calc_color_metric(img): 
    ih, iw, ich = img.shape
    img1 = img[0: np.int(ih / 2), 0:iw]
    img2 = img[np.int(ih / 2):ih, 0:iw]

    hist_1 = cv2.calcHist([img1],[0],None,[256],[0,256])
    hist_2 = cv2.calcHist([img2],[0],None,[256],[0,256])

    blue=cv2.compareHist(hist_1,hist_2,cv2.HISTCMP_BHATTACHARYYA)

    hist_1 = cv2.calcHist([img1],[1],None,[256],[0,256])
    hist_2 = cv2.calcHist([img2],[1],None,[256],[0,256])

    green=cv2.compareHist(hist_1,hist_2,cv2.HISTCMP_BHATTACHARYYA)

    hist_1 = cv2.calcHist([img1],[2],None,[256],[0,256])
    hist_2 = cv2.calcHist([img2],[2],None,[256],[0,256])

    red=cv2.compareHist(hist_1,hist_2,cv2.HISTCMP_BHATTACHARYYA)

    metric = (blue + green + red)/3

    return metric

