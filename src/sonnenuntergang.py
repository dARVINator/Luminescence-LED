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

r = 155
g = 147
b = 256.5
w = 250

durchlauf = 0

while durchlauf == 0:

   #Diese Schleife wird getriggert wenn sie eine bestimmte Zeit erreicht hat. 
   #Wenn dieser erreicht wird werden die Farbwert summierungen geändert.   

    if r == 155 and g == 147 and b == 256.5 and w == 250:

        while r <= 155 and g <= 147 and b <= 156.5 and w <= 0:
            #erste Schleife

            r = r - 0
            g = g - 0
            b = b - 2 
            w = w - 5
            

            pi.set_PWM_dutycycle(RED, r)
            pi.set_PWM_dutycycle(GREEN, g)
            pi.set_PWM_dutycycle(BLUE, b)
            pi.set_PWM_dutycycle(WHITE, w)
            time.sleep(0.5)

        print ("erste Schleife")

        print (r)
        print (g)
        print (b)
        print (w)  

        while r <= 155 and g <= 114.5 and b <= 91 and w <= 0:
            #zweite Schleife

            r = r - 0
            g = g - 2.5
            b = b - 5
            w = w - 0

            pi.set_PWM_dutycycle(RED, r)
            pi.set_PWM_dutycycle(GREEN, g)
            pi.set_PWM_dutycycle(BLUE, b)
            pi.set_PWM_dutycycle(WHITE, w)
            time.sleep(0.5) 

        print ("zweite Schleife")

        print (r)
        print (g)
        print (b)
        print (w)  

        while r <= 115 and g <= 34.5 and b <= 11.5 and w <= 0:
            #dritte Schleife 
            
            r = r - 2
            g = g - 4
            b = b - 4
            w = w - 0

            pi.set_PWM_dutycycle(RED, r)
            pi.set_PWM_dutycycle(GREEN, g)
            pi.set_PWM_dutycycle(BLUE, b)
            pi.set_PWM_dutycycle(WHITE, w)
            time.sleep(0.5) 

        print ("dritte Schleife")

        print (r)
        print (g)
        print (b)
        print (w) 

        

        while r <= 0 and g <= 0 and b <= 0 and w <= 0:
            
            #fünfte Schleife

            r = r - 4.5
            g = g - 1.5
            b = b - 0
            w = w - 0
            
            pi.set_PWM_dutycycle(RED, r)
            pi.set_PWM_dutycycle(GREEN, g)
            pi.set_PWM_dutycycle(BLUE, b)
            pi.set_PWM_dutycycle(WHITE, w)
            time.sleep(0.5)

        print ("fünfte Schleife")

        print (r)
        print (g)
        print (b)
        print (w)

        durchlauf = durchlauf + 1
        print ("Jetzt ist Tag")