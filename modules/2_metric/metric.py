import cv2
import numpy as np
import math

def calc_metric(image):
    img = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY) 
    img = cv2.resize(img, (60, 80))
    ih, iw = img.shape
    img1 = img[0: np.int(ih / 2), 0:iw]
    img2 = img[np.int(ih / 2):ih, 0:iw]

    hist_1 = cv2.calcHist([img1],[0],None,[256],[0,256])
    hist_2 = cv2.calcHist([img2],[0],None,[256],[0,256])
    
    '''
    sum_hist_1 = 0
    sum_hist_2 = 0
    for i in range (len(hist_1)):
        sum_hist_1 += hist_1[i]
        sum_hist_2 += hist_2[i]
    sum_hist = math.sqrt(sum_hist_1 * sum_hist_2)

    sum = 0
    for i in range (len(hist_1)):
        sum += math.sqrt(hist_1[i] * hist_2[i]) / sum_hist
    metric = math.sqrt(1 - sum)
    '''

    metric = cv2.compareHist(hist_1,hist_2,cv2.HISTCMP_BHATTACHARYYA)

    return metric