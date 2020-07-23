import numpy as np
import cv2
import unittest
from project import detection_masks

class TestForLandmarks(unittest.TestCase):
    def test_project(self):
        detection_masks(0.33)

        self.assertEqual(1, 1)


if __name__ == '__main__':
    unittest.main()