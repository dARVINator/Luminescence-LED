# This Python file uses the following encoding: utf-8
import os
import sys
import termios
import tty
import pigpio
import time

pigpio.exceptions = False

#Hier werden die GPIO Pins als Variable deklariert.
#Das ist einfacher und übersichtlicher.

RED   = 17
GREEN = 22
BLUE  = 24
WHITE = 23

pi = pigpio.pi()

#Hier werden die Farbwerte festgelegt. 

r = 0
g = 1
b = 2
w = 0

pi.set_PWM_dutycycle(RED, r)
pi.set_PWM_dutycycle(GREEN, g)
pi.set_PWM_dutycycle(BLUE, b)
pi.set_PWM_dutycycle(WHITE, w)
time.sleep(0.5)

