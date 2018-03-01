import RPi.GPIO as GPIO #Use GPIO library
import time #Use time library

GPIO.setwarnings(False)

ledPin = 11    # pin11 is connected to the led anode (+ve pin), cathode(-ve pin) connected to pin9 GND
buttonPin = 16  # pin 16 is connected to the button - other button pin is connected to gnd - pin 14
GPIO.setmode(GPIO.BOARD)  # Numbers GPIOs by physical location

GPIO.setup(ledPin, GPIO.OUT)    #set ledPin's mode as output
GPIO.output(ledPin, GPIO.LOW)   #initially turn off the led

GPIO.setup(buttonPin, GPIO.IN, pull_up_down=GPIO.PUD_UP)    #Set buttonPin as input and enable pullup resistor

while True: #Loop indefinitely
  GPIO.wait_for_edge(buttonPin, GPIO.FALLING) #Button was pressed
  print('Button Pressed') #Display button pressed
  GPIO.output(ledPin, GPIO.HIGH)  # Turn led on
  GPIO.wait_for_edge(buttonPin, GPIO.RISING) #Button was released
  GPIO.output(ledPin, GPIO.LOW)  # Turn led off

GPIO.cleanup(); #Clean up when exiting the program