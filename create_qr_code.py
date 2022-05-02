#pip install pyqrcode
#pip install pypng

import pyqrcode
import png
from pyqrcode import QRCode
import cv2
import numpy as np

#string which represents the QR code
s = "https://github.com"

#output file name
filename = "qrcode.png"

#generate QR code
img = pyqrcode.create(s)

#create and save the svg file
img.svg("myqr.svg", scale = 8)

#create and save the png file
img.png("myqr.png", scale = 6)
