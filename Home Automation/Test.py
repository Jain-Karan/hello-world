
#Test.py
#!/usr/bin/python
import cv
import getpass
src = cv.LoadImage("/home/"+getpass.getuser()+"/test.png")
cv.NamedWindow("RGB",cv.CV_WINDOW_AUTOSIZE)
cv.ShowImage("RGB", src)
cv.WaitKey(500)
cv.DestroyWindow("RGB")
