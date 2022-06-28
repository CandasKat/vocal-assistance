import os
import RPi.GPIO as GPIO

def light_led(query):
    GPIO.setmode(GPIO.BOARD)
    GPIO.setwarnings(False)

    LED = 7

    GPIO.setup(LED, GPIO.OUT)

    if query == "allumer" : 
        GPIO.output(LED, GPIO.HIGH)
        
    elif query == "éteindre":
        GPIO.output(LED, GPIO.LOW)




