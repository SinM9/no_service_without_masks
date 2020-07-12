import os
import numpy as np
import cv2 as cv
from detector import nms
from detector import iou


def test_nms():
    print('\nTest nms')
    boxes = [ [24, 17, 99, 146], [38, 38, 126, 172], [30, 88, 180, 193] ]
    probs = [0.81, 0.89, 0.92]
    indices = []

    nms(boxes, probs, 0.4, indices)

    assert(len(indices) == 2)

def test_iou():
    print('\nTest iou')
    a = [21, 27, 131, 177]
    b = [53, 56, 161, 208]

    assert(iou(a, b) - 0.401993 <= 1e-5)


test_nms()
test_iou()

