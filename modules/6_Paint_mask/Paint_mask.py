import os
import cv2
import numpy as np
from PIL import Image
from detector import detect
from landmarks import landmarks_35

data_folder = os.path.join(os.path.dirname(__file__), '..', '..', 'data')
image=os.path.join(data_folder,'no_mask.png')
img=cv2.imread(image)
img_clone=cv2.imread(image)
mask=Image.open(r"D:\openvino_practice\data\mask_png.PNG")
img_clone=cv2.cvtColor(img_clone,cv2.COLOR_BGR2RGB)
im_pil=Image.fromarray(img_clone)
boxes=detect(data_folder,image)
for box in boxes:
    box=boxes[0]
    imagecut=img[box[1]:box[3],box[0]:box[2]]
    x,y=landmarks_35(imagecut)
    x = x[19]
    y = y[19]
    Image.Image.paste(im_pil, mask, (-25, y))
    im_pil.show()
