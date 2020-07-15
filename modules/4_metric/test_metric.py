import os
import numpy as np
import cv2
import unittest
from metric import calc_metric

class TestForLandmarks(unittest.TestCase):
    def test_metric(self):
        data_folder = os.path.join(os.path.dirname(__file__), '..', '..', 'data')

        img_file = os.path.join(data_folder, 'mask.png')
        image = cv2.imread(img_file)


        metric = calc_metric(image)

        self.assertEqual(metric > 0, 1)
        self.assertEqual(metric < 1, 1)


    def test_metric_two_pictures(self):
        data_folder = os.path.join(os.path.dirname(__file__), '..', '..', 'data')

        img_file = os.path.join(data_folder, 'mask.png')
        image_mask = cv2.imread(img_file)

        img_file = os.path.join(data_folder, 'no_mask.png')
        image_no_mask = cv2.imread(img_file)

        metric_mask = calc_metric(image_mask)
        metric_no_mask = calc_metric(image_no_mask)

        self.assertEqual(metric_mask > metric_no_mask, 1)


if __name__ == '__main__':
    unittest.main()
