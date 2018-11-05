import RPi.GPIO as GPIO #Use GPIO library
import time #Use time library

pirPin = 7  # pin 7 is connected to output from the PIR motion sensor, 5V to pin 2, GND to pin 6
buzzerPin = 11  # pin 11 is connected to the +ve buzzer pin; -ve connected to pin 9 GND
GPIO.setmode(GPIO.BOARD)  # Numbers GPIOs by physical location

GPIO.setup(pirPin, GPIO.IN); #set the pirPin as input
GPIO.setup(buzzerPin, GPIO.OUT); #set the buzzer pin as output
GPIO.output(buzzerPin, GPIO.LOW) #initially turn off the buzzer

#define alarm events
def soundAlarm(pirPin):
  #sound alarm (for 2 seconds )
  print("Sound Alarm")
  GPIO.output(buzzerPin, GPIO.HIGH)  # Turn buzzer on
  time.sleep(2) # Pause for 2 seconds
  turnOffAlarm()  # Turn buzzer off

def turnOffAlarm():
  #turn off alarm
  GPIO.output(buzzerPin, GPIO.LOW)  # Turn buzzer off

#adding a callback function when the pir sensor output rises when motion is detected
GPIO.add_event_detect(pirPin, GPIO.RISING, callback=soundAlarm);

#try catch block to perform GPIO cleanup
try:
  while True:
    pass
except KeyboardInterrupt:
  print("You ended the program")
finally:
  #clean up the GPIO pins
  GPIO.cleanup()
