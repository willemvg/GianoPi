import RPi.GPIO as GPIO
import time

#set the board mode to BCM for GPIO pin referencing
GPIO.setmode(BCM)

#constants
TRIGGER1 = 17
ECHO1 = 18
TRIGGER2 = 23
ECHO2 = 24

#set up triggers as outputs and echoes as inputs
GPIO.setmode(TRIGGER1,GPIO.OUT)
GPIO.setmode(ECHO1, GPIO.IN)
GPIO.setmode(TRIGGER2,GPIO.OUT)
GPIO.setmode(ECHO2, GPIO.IN)

def getDistance(sensor): #sensor is either 1 or 2: refers to the 2 ultrasonic sensors
    if (sensor==1):
        GPIO.output(TRIGGER1, True)
        time.sleep(10)
        while (GPIO.input(TRIGGER1) == 0):
            start = time.time()
        while (GPIO.input(TRIGGER1) == 1):
            finish = time.time()
    elif (sensor==2):
        GPIO.output(TRIGGER2, True)
        time.sleep(10)
        while (GPIO.input(TRIGGER2) == 0):
            start = time.time()
        while (GPIO.input(TRIGGER2) == 1):
            finish = time.time()
    return finish - start
