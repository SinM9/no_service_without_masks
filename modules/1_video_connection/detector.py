import os
import cv2
import numpy as np
from openvino.inference_engine import IECore

def detect(image):
    ie = IECore()

    data_folder = os.path.join(os.path.dirname(__file__), '..', '..', 'data')
    model_xml = os.path.join(data_folder, 'face-detection-0104.xml')
    model_bin = os.path.join(data_folder, 'face-detection-0104.bin')

    net = ie.read_network(model = model_xml, weights = model_bin)

    if len(net.inputs["image"].layout) == 4:
        n, c, h, w = net.inputs["image"].shape

    ih, iw = image.shape[:-1]

    if (ih, iw) != (h, w):
        image = cv2.resize(image, (w, h))

    image = image.transpose((2, 0, 1))

    out_blob = next(iter(net.outputs))

    data = {}
    data["image"] = image

    exec_net = ie.load_network(network = net, device_name = "CPU")

    res = exec_net.infer(inputs = data)

    res = res[out_blob]
    boxes, classes, probabilities = [], [], []
    data = res[0][0]

    for number, proposal in enumerate(data):
        if proposal[2] > 0.3:
            label = np.int(proposal[1])
            xmin = np.int(iw * proposal[3])
            ymin = np.int(ih * proposal[4])
            xmax = np.int(iw * proposal[5])
            ymax = np.int(ih * proposal[6])
            boxes.append([xmin, ymin, xmax, ymax])
            classes.append(label)
            probabilities.append(proposal[2])

    return boxes

