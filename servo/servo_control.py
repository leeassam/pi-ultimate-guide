import RPi.GPIO as GPIO #Use GPIO library
import time #Use time library

#define pins
signal_pin = 12

GPIO.setmode(GPIO.BOARD)  # Numbers GPIOs by physical location

#set pins as output to motor driver
GPIO.setup(signal_pin, GPIO.OUT)

#create a PWM instance with default frequency of 100 Hz
pwm = GPIO.PWM(enable_pin, 100);

#start pwm, 0 is the duty cycle
pwm.start(0);

while True: #Loop indefinitely
  #peform a full servo sweep
  for dutyCycle in range (0, 100):
    pwm.changeDutyCycle(dutyCycle)
    sleep(0.05)
    
  for dutyCycle in range (100, 0):
    pwm.changeDutyCycle(dutyCycle)
    sleep(0.05)
GPIO.cleanup(); #Clean up when exiting the program

#https://sourceforge.net/p/raspberry-gpio-python/wiki/PWM/