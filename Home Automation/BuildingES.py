#BuildingES.py
#!/usr/bin/python

import cv  #import the openCV lib to python
import serial #import the pyserial module
import getpass

#Module -1: Image Processing
hc = cv.Load(“/home/"+getpass.getuser()+"/haarcascade_frontalface_default.xml”)
img = cv.LoadImage(“/home/"+getpass.getuser()+"/beautiful-faces.jpg”, 0)
faces = cv.HaarDetectObjects(img, hc, cv.CreateMemStorage())
a=1
print(faces)
for (x, y, w, h), n in faces:
    cv.Rectangle(img, (x, y), (x+w, y+h), 255)
cv.SaveImage(“faces_detected.jpg”, img)
dst=cv.LoadImage(“faces_detected.jpg”)
cv.NamedWindow(“Face Detected”, cv.CV_WINDOW_AUTOSIZE)
cv.ShowImage(“Face Detected”, dst)
cv.WaitKey(5000)
cv.DestroyWindow(“Face Detected”)

#Module -2: Trigger Pyserial
if faces==[]:

	ser=serial.Serial(‘/dev/ttyUSB0’,9600)
	print(ser)
	ser.write(‘N’)
else:

	ser=serial.Serial(‘/dev/ttyUSB0’,9600)
	print(ser)
	ser.write(‘Y’)


