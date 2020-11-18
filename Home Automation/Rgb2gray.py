#Rgb2gray.py
#!/usr/bin/python
import cv
src = cv.LoadImage("/home/jayneil/12.png")
cv.NamedWindow("RGB", cv.CV_WINDOW_AUTOSIZE)
cv.ShowImage("RGB", src)
cv.WaitKey(500)
cv.DestroyWindow("RGB")
dst = cv.CreateImage(cv.GetSize(src), cv.IPL_DEPTH_8U, 1)
cv.CvtColor(src, dst, cv.CV_RGB2GRAY)
cv.NamedWindow("GRAY", cv.CV_WINDOW_AUTOSIZE)
cv.ShowImage("GRAY", dst)
cv.WaitKey(1000)
cv.DestroyWindow("GRAY")

