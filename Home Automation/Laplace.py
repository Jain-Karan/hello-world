#Laplace.py
#!/usr/bin/python
import cv
src = cv.LoadImage("/home/jayneil/12.png")
print(src)
cv.NamedWindow("RGB", cv.CV_WINDOW_AUTOSIZE)
cv.ShowImage("RGB", src)
cv.WaitKey(1000)
cv.DestroyWindow("RGB")
dst = cv.CreateImage(cv.GetSize(src), cv.IPL_DEPTH_16S, 3)
laplace = cv.Laplace(src, dst)
cv.SaveImage("/home/jayneil/laplace.png", dst)
temp=cv.LoadImage("/home/jayneil/laplace.png")
cv.NamedWindow("Laplace", cv.CV_WINDOW_AUTOSIZE)
cv.ShowImage("Laplace", temp)
cv.WaitKey(2000)
cv.DestroyWindow("Laplace")

