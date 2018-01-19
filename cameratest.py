import sys
import time
import logging
import cv2
import cscore as cs
import numpy as np
from networktables import NetworkTables

camera = cs.UsbCamera("usbcam", 0)

camera.setVideoMode(cs.VideoMode.PixelFormat.kMJPEG, 320, 240, 30)

cvsink = cs.CvSink("cvsink")
cvsink.setSource(camera)

mjpegServer = cs.MjpegServer("httpserver", 8081)
mjpegServer.setSource(camera)

cvSource = cs.CvSource("cvsource", cs.VideoMode.PixelFormat.kMJPEG, 320, 240, 30)
cvServer = cs.MjpegServer("cvhttpserver", 8082)
cvServer.setSource(cvSource)

frame = np.zeros(shape=(240, 320, 3), dtype=np.uint8)
flip = np.zeros(shape=(240, 320, 3), dtype=np.uint8)

while True:
    time, frame = cvsink.grabFrame(frame)

    if time == 0:
        print("Error: " + cvsink.getError())
        continue

    print("Got frame: at time " + time + " " + test.shape)
    cv2.flip(frame, flipCode=0, dst=flip)
    cvSource.putFrame(flip)
        
