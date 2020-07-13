import os
import cv2
import numpy as np
from openvino.inference_engine import IECore


def landmarks_5(image):

    data_folder = os.path.join(os.path.dirname(__file__), '..', '..', 'data')

    ie = IECore()
   
    model_xml = os.path.join(data_folder, 'landmarks-regression-retail-0009.xml')
    model_bin = os.path.join(data_folder, 'landmarks-regression-retail-0009.bin')

    net = ie.read_network(model=model_xml, weights=model_bin)


    if len(net.inputs["0"].layout) == 4:
        n, c, h, w = net.inputs["0"].shape


    ih, iw = image.shape[:-1]
    if (ih, iw) != (h, w):
        image = cv2.resize(image, (w, h))
    image = image.transpose((2, 0, 1))

    out_blob = next(iter(net.outputs))


    data = {}
    data["0"] = image

    exec_net = ie.load_network(network=net, device_name="CPU")
    res = exec_net.infer(inputs=data)
    res = res[out_blob]
    data = res[0]
    x = []
    y = []
    i = 0
    for number, proposal in enumerate(data):
        if (i % 2 == 0):
            x.append(np.int(proposal[0][0] * iw))
        else:
            y.append(np.int(proposal[0][0] * ih))
        i += 1

    return x, y




def landmarks_35(image):
    data_folder = os.path.join(os.path.dirname(__file__), '..', '..', 'data')

    ie = IECore()
   
    model_xml = os.path.join(data_folder, 'facial-landmarks-35-adas-0002.xml')
    model_bin = os.path.join(data_folder, 'facial-landmarks-35-adas-0002.bin')

    net = ie.read_network(model=model_xml, weights=model_bin)


    if len(net.inputs["data"].layout) == 4:
        n, c, h, w = net.inputs["data"].shape


    ih, iw = image.shape[:-1]
    if (ih, iw) != (h, w):
        image = cv2.resize(image, (w, h))
    image = image.transpose((2, 0, 1))

    out_blob = next(iter(net.outputs))


    data = {}
    data["data"] = image

    exec_net = ie.load_network(network=net, device_name="CPU")
    res = exec_net.infer(inputs=data)
    res = res[out_blob]
    data = res[0]
    x = []
    y = []
    i = 0

    for number, proposal in enumerate(data):
        if (i % 2 == 0):
            x.append(np.int(proposal * iw))
        else:
            y.append(np.int(proposal * ih))
        i += 1

    return x, y