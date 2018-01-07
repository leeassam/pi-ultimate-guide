import RPi.GPIO as GPIO #Use GPIO library
import time #Use time library

pirPin = 11  # pin 11 is connected to output from the PIR motion sensor
GPIO.setmode(GPIO.BOARD)  # Numbers GPIOs by physical location

while True: #Loop indefinitely
    input_state = GPIO.input(pirPin) #Retrieve the state of the button pin
    if input_state == True:    #If readling is HIGH, there is output from the motion sensor
        print('Motion Detected') #DMotion was detected
        time.sleep(0.5) #Wait for 1/2 second

GPIO.cleanup(); #Clean up when exiting the program