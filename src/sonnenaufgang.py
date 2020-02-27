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
g = 0
b = 0
w = 0

durchlauf = 0

while durchlauf == 0:

   #Diese Schleife wird getriggert wenn sie eine bestimmte Zeit erreicht hat. 
   #Wenn dieser erreicht wird werden die Farbwert summierungen geändert.   

    if r == 0 and g == 0 and b == 0 and w == 0:

        while r <= 110 and g <= 33 and b <= 11 and w <= 0:

            #erste SChleife

            r = r + 5
            g = g + 1.5 
            b = b + 0.5
            w = w + 0

            pi.set_PWM_dutycycle(RED, r)
            pi.set_PWM_dutycycle(GREEN, g)
            pi.set_PWM_dutycycle(BLUE, b)
            pi.set_PWM_dutycycle(WHITE, w)
            time.sleep(0.5)

        print ("erste SChleife") 

        #if r == 110 and g == 33 and b == 11 and w == 0:

        while r <= 173 and g <= 54 and b <= 11 and w <= 0:
            
            #zweite Schleife

            r = r + 4.5
            g = g + 1.5
            b = b + 0
            w = w + 0
            
            pi.set_PWM_dutycycle(RED, r)
            pi.set_PWM_dutycycle(GREEN, g)
            pi.set_PWM_dutycycle(BLUE, b)
            pi.set_PWM_dutycycle(WHITE, w)
            time.sleep(0.5)

        print ("zweite Schleife")

        #if r == 173 and g == 54 and b == 11 and w == 0:

        while r <= 215 and g <= 114 and b <= 11 and w <= 0:

        #dritte SChleife 

            r = r + 3.5
            g = g + 5
            b = b + 0
            w = w + 0

            pi.set_PWM_dutycycle(RED, r)
            pi.set_PWM_dutycycle(GREEN, g)
            pi.set_PWM_dutycycle(BLUE, b)
            pi.set_PWM_dutycycle(WHITE, w)
            time.sleep(0.5)  

        print ("dritte Schleife")

        #if r == 215 and g == 114 and b == 11 and w == 0:

        while r <= 255 and g <= 194 and b <= 91 and w <= 0:

        #vierte Schleife 
            
            r = r + 2
            g = g + 4
            b = b + 4
            w = w + 0

            pi.set_PWM_dutycycle(RED, r)
            pi.set_PWM_dutycycle(GREEN, g)
            pi.set_PWM_dutycycle(BLUE, b)
            pi.set_PWM_dutycycle(WHITE, w)
            time.sleep(0.5) 

        print ("vierte Schleife")

        #if r == 255 and g == 194 and b == 91 and w == 0:

        while r <= 255 and g <= 226.5 and b <= 156 and w <= 0:

            #fünfte Schleife

            r = r + 0
            g = g + 2.5
            b = b + 5
            w = w + 0

            pi.set_PWM_dutycycle(RED, r)
            pi.set_PWM_dutycycle(GREEN, g)
            pi.set_PWM_dutycycle(BLUE, b)
            pi.set_PWM_dutycycle(WHITE, w)
            time.sleep(0.5) 

        print ("fünfte Schleife")

        #if r == 255 and g == 226.5 and b == 156 and w == 0:

        while r <= 255 and g <= 255 and b <= 255 and w <= 255:
        
        #sechste Schleife

            r = r + 0
            g = g + 0
            b = b + 2 
            w = w + 5
            

            pi.set_PWM_dutycycle(RED, r)
            pi.set_PWM_dutycycle(GREEN, g)
            pi.set_PWM_dutycycle(BLUE, b)
            pi.set_PWM_dutycycle(WHITE, w)
            time.sleep(0.5)

            

        print ("sechste Schleife")

    durchlauf + 1