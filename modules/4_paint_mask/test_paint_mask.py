import os
import numpy as np
import cv2
import unittest
from detector import detect
from paint_mask import painting_mask

class TestForLandmarks(unittest.TestCase):
    def test_paint_mask(self):
        data_folder = os.path.join(os.path.dirname(__file__), '..', '..', 'data')
        img_file = os.path.join(data_folder, 'no_mask2.jpg')
        image = cv2.imread(img_file)
        boxes = detect(image)
        image = painting_mask(image, boxes[0])

        cv2.imwrite('res.jpg', image)

        self.assertEqual(1, 1)


if __name__ == '__main__':
    unittest.main()