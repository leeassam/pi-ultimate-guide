import RPi.GPIO as GPIO #Use GPIO library
import time #Use time library

ledPin = 11    # pin11 is connected to the led anode (+ve pin)
buttonPin = 16  # pin 16 is connected to the button - other button pin is connected to gnd - pin 14
GPIO.setmode(GPIO.BOARD)  # Numbers GPIOs by physical location

GPIO.setup(buttonPin, GPIO.IN, pull_up_down=GPIO.PUD_UP)    #Set buttonPin as input and enable pullup resistor

while True: #Loop indefinitely
    input_state = GPIO.input(buttonPin) #Retrieve the state of the button pin
    if input_state == False:    #If readling is LOW, button is pressed
        print('Button Pressed') #Display button pressed
        GPIO.output(ledPin, GPIO.HIGH)  # Turn led on
        time.sleep(0.2) #Wait for slight delay
    else :
        GPIO.output(ledPin, GPIO.LOW)  # Turn led off
        time.sleep(0.2) #Wait for slight delay