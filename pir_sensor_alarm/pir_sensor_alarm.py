import RPi.GPIO as GPIO #Use GPIO library
import time #Use time library

#GPIO.setwarnings(False)

pirPin = 11  # pin 11 is connected to output from the PIR motion sensor, 5V to pin 2, GND to pin 6
buzzerPin = 18  # pin 18 is connected to the +ve buzzer pin; -ve connected to pin 20 GND
GPIO.setmode(GPIO.BOARD)  # Numbers GPIOs by physical location
GPIO.setup(pirPin, GPIO.IN) #set the pirPin as an input
GPIO.setup(ledPin, GPIO.OUT) #set the ledPin as an output

#define alarm events
define soundAlarm(pirPin):
  #sound alarm (for 3 seconds ?)
  GPIO.output(buzzerPin, GPIO.HIGH)  # Turn buzzer on
  #time.sleep(3) # Pause for 3 seconds

define turnOffAlarm(pirPin):
  #turn off alarm
    GPIO.output(buzzerPin, GPIO.LOW)  # Turn buzzer off

#adding a callback function when the pir sensor output rises when motion is detected
#further edges are ignored for 300 ms for switch bounce handling
GPIO.add_event_detect(pirPin, GPIO.RISING, callback=alarm, bouncetime=300);

#adding a callback function when the pir sensor output falls when motion stops
#further edges are ignored for 300 ms for switch bounce handling
GPIO.add_event_detect(pirPin, GPIO.FALLING, callback=turnOffAlarm, bouncetime=300);

GPIO.cleanup(); #Clean up when exiting the program