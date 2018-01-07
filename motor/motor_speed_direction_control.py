import RPi.GPIO as GPIO #Use GPIO library
import time #Use time library

#define pins
enable_pin = 12
in1_pin = 16
in2_pin = 18

GPIO.setmode(GPIO.BOARD)  # Numbers GPIOs by physical location

#set pins as output to motor driver
GPIO.setup(enable_pin, GPIO.OUT)
GPIO.setup(in1_pin, GPIO.OUT)
GPIO.setup(in2_pin, GPIO.OUT)

#create a PWM instance with default frequency of 500 Hz
pwm = GPIO.PWM(enable_pin, 500);

#start pwm, 0 is the duty cycle
pwm.start(0);

#turn motor clockwise
def clockwise():
  GPIO.output(in1_pin, True)
  GPIO.output(in2_pin, False)

#turn motor counter clockwise
def counter_clockwise():
  GPIO.output(in1_pin, False)
  GPIO.output(in2_pin, True)

while True: #Loop indefinitely
#get input direction and speed from the user
  cmd = raw_input("Command, f/r 0...9, E.g. f5 :")
  direction = cmd[0];

#adjust direction of spin
  if direction == "f":
    clockwise();
  else:
    counter_clockwise();
 
#adjust speed
  speed = int(cmd[1]) * 10
  pwm.changeDutyCycle(speed)

GPIO.cleanup(); #Clean up when exiting the program