# This Python file uses the following encoding: utf-8
import os
import sys
import termios
import tty
import pigpio
import time

pigpio.exceptions = False

def sunrise():
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
        
        ticks1 = 0
        ticks2 = 0
        ticks3 = 0
        ticks4 = 0

        while ticks1 <= 44:

            #erste Schleife

            r = r + 2.5
            g = g + 0.8
            b = b + 0.25
            w = w + 0

            pi.set_PWM_dutycycle(RED, r)
            pi.set_PWM_dutycycle(GREEN, g)
            pi.set_PWM_dutycycle(BLUE, b)
            pi.set_PWM_dutycycle(WHITE, w)
            time.sleep(0.25)

            ticks1 = ticks1 + 1

            

        print ("erste Schleife") 

        print (r)
        print (g)
        print (b)
        print (w)

        while ticks2 <= 40:

            #zweite Schleife

            r = r + 1
            g = g + 1.32
            b = b + 2
            w = w + 0

            pi.set_PWM_dutycycle(RED, r)
            pi.set_PWM_dutycycle(GREEN, g)
            pi.set_PWM_dutycycle(BLUE, b)
            pi.set_PWM_dutycycle(WHITE, w)
            time.sleep(0.25)

            ticks2 = ticks2 + 1

            

        print ("zweite Schleife") 

        print (r)
        print (g)
        print (b)
        print (w)

        while ticks3 <= 37:

            #dritte Schleife

            r = r + 0.05
            g = g + 1.5
            b = b + 1.6
            w = w + 0

            pi.set_PWM_dutycycle(RED, r)
            pi.set_PWM_dutycycle(GREEN, g)
            pi.set_PWM_dutycycle(BLUE, b)
            pi.set_PWM_dutycycle(WHITE, w)
            time.sleep(0.25)

            ticks3 = ticks3 + 1

            

        print ("dritte Schleife") 

        print (r)
        print (g)
        print (b)
        print (w)

        while ticks4 <= 101:

            #vierte Schleife

            r = r + 0
            g = g + 0
            b = b + 1
            w = w + 2.5

            pi.set_PWM_dutycycle(RED, r)
            pi.set_PWM_dutycycle(GREEN, g)
            pi.set_PWM_dutycycle(BLUE, b)
            pi.set_PWM_dutycycle(WHITE, w)
            time.sleep(0.25)

            ticks4 = ticks4 + 1

            

        print ("vierte Schleife") 

        print (r)
        print (g)
        print (b)
        print (w)
        
        durchlauf = +1
        print ("Jetzt ist Tag")
sunrise()