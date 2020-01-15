import pigpio
import time

RED   = 17
GREEN = 22
BLUE  = 24

pi = pigpio.pi()

r = 0
g = 0 
b = 0

while True:

    pi.set_PWM_dutycycle(RED, r)
    pi.set_PWM_dutycycle(GREEN, g)
    pi.set_PWM_dutycycle(BLUE, b)
    time.sleep(1)
    
    r = r + 5
    g = g + 1.5 
    b = b + 0.5
    if r == 110:

        r = r + 4.5
        g = g + 1.5
        b = b + 0

        pi.set_PWM_dutycycle(RED, r)
        pi.set_PWM_dutycycle(GREEN, g)
        pi.set_PWM_dutycycle(BLUE, b)
        time.sleep(1)
    if r == 173:

        r = r + 3.5
        g = g + 5
        b = b + 0

        pi.set_PWM_dutycycle(RED, r)
        pi.set_PWM_dutycycle(GREEN, g)
        pi.set_PWM_dutycycle(BLUE, b)
        time.sleep(1)    
        
        
