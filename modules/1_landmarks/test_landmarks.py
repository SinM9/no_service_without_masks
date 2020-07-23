import os
import numpy as np
import cv2
import unittest
from landmarks import landmarks_35
from landmarks import landmarks_5

class TestForLandmarks(unittest.TestCase):
    def test_landmarks_5(self):
        data_folder = os.path.join(os.path.dirname(__file__), '..', '..', 'data')
        img_file = os.path.join(data_folder, 'o.png')
        image = cv2.imread(img_file)

        x, y = landmarks_5(image)

        # tmp_image = cv2.imread(img_file)
        # for i in range(len(x)):
        #     cv2.circle(tmp_image,(x[i],y[i]), 2, (0,0,255), -1)
        # cv2.imwrite("out.png", tmp_image)

        self.assertEqual(len(x), 5)
        self.assertEqual(len(y), 5)

    def test_landmarks_35(self):
        data_folder = os.path.join(os.path.dirname(__file__), '..', '..', 'data')
        img_file = os.path.join(data_folder, 'o.png')
        image = cv2.imread(img_file)

        x, y = landmarks_35(image)

        # tmp_image = cv2.imread(img_file)
        # for i in range(len(x)):
        #     cv2.circle(tmp_image,(x[i],y[i]), 2, (0,0,255), -1)
        # cv2.imwrite("out.png", tmp_image)

        self.assertEqual(len(x), 35)
        self.assertEqual(len(y), 35)


if __name__ == '__main__':
    unittest.main()
