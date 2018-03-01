#!/bin/bash

DATE=$(date +"%Y-%m-%d_%H%M")

mkdir /home/pi/Downloads/photos

fswebcam -r 1280x720 --no-banner /home/pi/Downloads/photos/$DATE.jpg
