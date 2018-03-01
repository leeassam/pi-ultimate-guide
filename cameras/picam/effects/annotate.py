from picamera import PiCamera
from time import sleep

camera = PiCamera()

camera.start_preview()
sleep(5)
camera.annotate_text = "I love Raspberry Pi!"
camera.capture('/home/pi/Downloads/photos/image.jpg')
camera.stop_preview()