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

#set clockwise as default -- arbitrary
GPIO.output(in1_pin, True)
GPIO.output(in2_pin, False)

#create a PWM instance with default frequency of 500 Hz
pwm = GPIO.PWM(enable_pin, 500);

#start pwm, 0 is the duty cycle
pwm.start(0);

while True: #Loop indefinitely
#get input speed from the user
  cmd = raw_input("Enter speed, 0...9, E.g. 5 :")
  direction = cmd[0];

  speed = int(cmd[0]) * 10
#change the duty cycle
  pwm.changeDutyCycle(speed)

GPIO.cleanup(); #Clean up when exiting the program

#https://sourceforge.net/p/raspberry-gpio-python/wiki/PWM/