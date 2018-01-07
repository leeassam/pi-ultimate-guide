import RPi.GPIO as GPIO #Use GPIO library
import time #Use time library

buttonPin = 16  # pin 16 is connected to the button - other button pin is connected to GND - pin 14
GPIO.setmode(GPIO.BOARD)  # Numbers GPIOs by physical location

GPIO.setup(buttonPin, GPIO.IN, pull_up_down=GPIO.PUD_UP)    #Set buttonPin as input and enable pullup resistor

while True: #Loop indefinitely
  input_state = GPIO.input(buttonPin) #Retrieve the state of the button pin
  if input_state == False:    #If readling is LOW, button has been pressed
    print('Button Pressed') #Display button pressed
    time.sleep(0.3) #Wait for 0.3 seconds for debouncing

GPIO.cleanup(); #Clean up when exiting the program