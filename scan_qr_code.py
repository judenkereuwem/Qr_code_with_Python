#scan and decode Qr code with webcam

import cv2
import pyqrcode
import png
from pyqrcode import QRCode
import numpy as np


cap = cv2.VideoCapture(0)
detector = cv2.QRCodeDetector()


while True:
    success, img = cap.read()
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    data, bbox, straight_qrcode = detector.detectAndDecode(img)
    if bbox is not None:
        print(f"QRCode data:\n{data}")

    cv2.imshow('Result', img)
    cv2.waitKey(1)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
