#Qr code decoder

import cv2
import pyqrcode
import png
from pyqrcode import QRCode
import numpy as np

#read qr image with opencv
img = cv2.imread('myqr.png')

#initialize the cv2 QRCode detector
detector = cv2.QRCodeDetector()

#detect and decode
data, bbox, straight_qrcode = detector.detectAndDecode(img)
if bbox is not None:
    print(f"QRCode data:\n{data}")

#display result
cv2.imshow("Image", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
