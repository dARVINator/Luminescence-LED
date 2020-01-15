from time import sleep
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

GPIO.setup(17, GPIO.OUT)
GPIO.setup(22, GPIO.OUT)
GPIO.setup(24, GPIO.OUT)

while True:
    GPIO.output(17, GPIO.HIGH)
    GPIO.output(22, GPIO.HIGH)
    GPIO.output(24,GPIO.HIGH)
    sleep(0.05)
    GPIO.output(17, GPIO.LOW)
    GPIO.output(22, GPIO.LOW)
    GPIO.output(24,GPIO.LOW)
    sleep(0.05) 
    
