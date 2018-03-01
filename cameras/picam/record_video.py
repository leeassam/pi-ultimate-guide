from picamera import PiCamera
from time import sleep

camera = PiCamera()

camera.start_preview()
camera.start_recording('/home/pi/Downloads/photos/video.h264')
sleep(10)
camera.stop_recording()
camera.stop_preview()

#view image
#omxplayer video.h264