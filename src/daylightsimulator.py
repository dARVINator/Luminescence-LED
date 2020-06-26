# This Python file uses the following encoding: utf-8
import os
import sys
import termios
import tty
import pigpio
import time
import datetime
import sunrise
import sunset

pigpio.exceptions = False

start = datetime.time(6, 00)
end = datetime.time(19, 30)
now = datetime.datetime.now()
print (now) 

def timer():
    if now >= start:
        sunrise.sunrise()
        print ("sonnenaufgang")
    elif now >= end:
        sunset.sunset()
        print ("sonnenuntergang")

while True:
    timer()
    time.sleep(60)
