import RPi.GPIO as GPIO #Use GPIO library
import time #Use time library


pirPin = 7  # pin 7 is connected to output from the PIR motion sensor
GPIO.setmode(GPIO.BOARD)  # Numbers GPIOs by physical location
GPIO.setup(pirPin, GPIO.IN) #set the pirPin as an input
count = 0; #number used as a reference to detect motion

while True: #Loop indefinitely
  input_state = GPIO.input(pirPin) #Retrieve the state of the button pin
  if input_state == True:    #If readling is HIGH, there is output from the motion sensor
    print("Motion Detected -- " + str(count))  #Motion was detected
    count+=1  #increment the count
    time.sleep(0.3) #Wait for 0.3 sec

GPIO.cleanup(); #Clean up when exiting the program