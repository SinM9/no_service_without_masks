import os
import detector
import numpy as np
import cv2 as cv
import unittest
from detector import detect

class TestForNMSandIOU(unittest.TestCase):
    
    def test_detect(self):
        data_folder = os.path.join(os.path.dirname(__file__), '..', '..', 'data')
        img_file=os.path.join(data_folder,'conference.png')
        box=detect(data_folder,img_file)
        k=0
        for i in box:
           k=k+1
        self.assertEqual(k,29)
if __name__ == '__main__':
    unittest.main()

