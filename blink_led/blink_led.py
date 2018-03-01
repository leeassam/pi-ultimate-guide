import RPi.GPIO as GPIO #Use GPIO library
import time #Use time library

GPIO.setwarnings(False)

ledPin = 11    # pin11 is connected to the led anode (+ve pin)
GPIO.setmode(GPIO.BOARD)       # Numbers GPIOs by physical location
GPIO.setup(ledPin, GPIO.OUT)   # Set ledPin's mode as output
GPIO.output(ledPin, GPIO.HIGH) # Set ledPin high(+3.3V) to turn on led

while True: # Continue looping indefinitely
  GPIO.output(ledPin, GPIO.HIGH)  # Turn led on
  time.sleep(1) # Pause for 1 second
  GPIO.output(ledPin, GPIO.LOW) # Turn led off
  time.sleep(1) # Pause for 1 second

GPIO.cleanup(); #Clean up when exiting the program