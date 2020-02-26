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
r = 0.0
g = 0.0
b = 0.0
w = 0.0

while True:
    

   #Diese Schleife wird getriggert wenn sie eine bestimmte Zeit erreicht hat. 
   #Die if prüfen ob es einen bestimmten Wert erreicht hat. 
   #Wenn dieser erreicht wird werden die Farbwert summierungen geändert.   
    
    if r == 0:

        #erste SChleife

        while r == 110 and g == 33 and b == 11 and w == 0:

            r = r + 5
            g = g + 1.5 
            b = b + 0.5
            w = w + 0

            pi.set_PWM_dutycycle(RED, r)
            pi.set_PWM_dutycycle(GREEN, g)
            pi.set_PWM_dutycycle(BLUE, b)
            pi.set_PWM_dutycycle(WHITE, w)
            time.sleep(1)

    print ("erste SChleife")

    if r == 110:

       #zweite Schleife 

        while r == 110 and g == 33 and b == 11 and w == 0:
            r = r + 4.5
            g = g + 1.5
            b = b + 0
            w = w + 0

         
            pi.set_PWM_dutycycle(RED, r)
            pi.set_PWM_dutycycle(GREEN, g)
            pi.set_PWM_dutycycle(BLUE, b)
            pi.set_PWM_dutycycle(WHITE, w)
            time.sleep(1)

    print ("zweite Schleife")

    if r == 173:

       #dritte SChleife 

        r = r + 3.5
        g = g + 5
        b = b + 0
        w = w + 0

        pi.set_PWM_dutycycle(RED, r)
        pi.set_PWM_dutycycle(GREEN, g)
        pi.set_PWM_dutycycle(BLUE, b)
        pi.set_PWM_dutycycle(WHITE, w)
        time.sleep(1)  

    if r == 215:

       #vierte Schleife 
        
        r = r + 2
        g = g + 4
        b = b + 4
        w = w + 0

        pi.set_PWM_dutycycle(RED, r)
        pi.set_PWM_dutycycle(GREEN, g)
        pi.set_PWM_dutycycle(BLUE, b)
        pi.set_PWM_dutycycle(WHITE, w)
        time.sleep(1) 

    if g == 194:

        #fünfte Schleife

        r = r + 0
        g = g + 2.5
        b = b + 5
        w = w + 0

        pi.set_PWM_dutycycle(RED, r)
        pi.set_PWM_dutycycle(GREEN, g)
        pi.set_PWM_dutycycle(BLUE, b)
        pi.set_PWM_dutycycle(WHITE, w)
        time.sleep(1) 

    if g == 255:

       #sechste Schleife

        r = r + 0
        g = g + 0
        b = b + 4 
        w = w + 10
        

        pi.set_PWM_dutycycle(RED, r)
        pi.set_PWM_dutycycle(GREEN, g)
        pi.set_PWM_dutycycle(BLUE, b)
        pi.set_PWM_dutycycle(WHITE, w)
        time.sleep(1)

    if w == 255:

        continue