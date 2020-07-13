import cv2
import numpy as np
from openvino.inference_engine import IECore


def nms(boxes, probabilities, threshold, indices):
    pre_indices = [0] * len(boxes)
    for i in range(len(boxes)):
        pre_indices[i] = i

    for i in range(len(boxes)):
        for j in range(i + 1, len(boxes)):
            iou_ = iou(boxes[i], boxes[j])
            if iou_ > threshold:
                if (probabilities[i] > probabilities[j]):
                    pre_indices[j] = -1
                else:
                    pre_indices[i] = -1
                    break
        k = i
        while k > 0:
            if pre_indices[k] != -1 and pre_indices[k - 1] != -1 and probabilities[pre_indices[k]] > probabilities[pre_indices[k - 1]]:
                tmp = pre_indices[i - k]
                pre_indices[i - k] = pre_indices[i - k - 1]
                pre_indices[i - k - 1] = tmp
            else:
                break
            k -= 1
    for i in range(len(boxes)):
        if (pre_indices[i] != -1):
            indices.append(pre_indices[i])


def iou(a, b):
    if (a[0] >= b[2] or b[0] >= a[2] or b[3] <= a[1] or a[3] <= b[1]):
        s = 0
    else:
        if (a[0] < b[0]):
            x1 = b[0]
        else:
            x1 = a[0]
        if (a[2] < b[2]):
            x2 = a[2]
        else:
            x2 = b[2]
        if (a[1] < b[1]):
            y1 = b[1]
        else:
            y1 = a[1]
        if (a[3] < b[3]):
            y2 = a[3]
        else:
            y2 = b[3]
        s = (x2 - x1) * (y2 - y1)
    return s / ((a[2] - a[0]) * (a[3] - a[1]) + (b[2] - b[0]) * (b[3] - b[1]) - s)



ie = IECore()

model_xml = "face-detection-0104.xml"
model_bin = "face-detection-0104.bin"

img_file = "conference.png"

net = ie.read_network(model = model_xml, weights = model_bin)

if len(net.inputs["image"].layout) == 4:
    n, c, h, w = net.inputs["image"].shape

image = cv2.imread(img_file)
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

indices = []

nms(boxes, probabilities, 0.45, indices)

size = len(boxes)
j = 0
cnt = 0

for i in range(size):
    if (j < len(indices) and indices[j] == i):
        j += 1
    else:
        boxes.pop(i - cnt)
        probabilities.pop(i - cnt)
        classes.pop(i - cnt)
        cnt += 1


tmp_image = cv2.imread(img_file)
for box in boxes:
    cv2.rectangle(tmp_image, (box[0], box[1]), (box[2], box[3]), (232, 35, 244), 2)
cv2.imwrite("out.png", tmp_image)
