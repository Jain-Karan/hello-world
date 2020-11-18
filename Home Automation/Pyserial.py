#Pyserial.py
#!usr/bin/python
import serial
ser=serial.Serial(‘/dev/ttyUSB1’,19200)
ser.write(“EFY\n”)
a=ser.readline()
print(a)
