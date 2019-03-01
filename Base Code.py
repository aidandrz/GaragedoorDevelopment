# Aidan Drzewicki

# Python Script That Will Run Garage Door
# Put this code into Raspbarian Python OS

# Load Libraries

import RPi.GPIO as GPIO
import time
from bottle import route, run, template

# Set up the GPIO pins
GPIO.setmode(GPIO.BOARD)
GPIO.setup(7, GPIO.OUT)
GPIO.setup(11,GPIO.OUT)
GPIO.output(7, True)
GPIO.output(11, True)

# Handle http requests to the root address
@route('/')
def index():
    return "Go Away."

# Handle http requests to /garagedoor
@route('/garagedoor/:doornum')
def garagedor(doornum=0):
    if doornum == '0':
        return 'No door number specified'

    elif doornum == '1':
    GPIO.output(7, False)
    time.sleep(.8)
    GPIO.output(7, True)
    return 'Door number 1 cycled.'

    elif doornum == '2':
    GPIO.output(11, False)
    time.sleep(.8)
    GPIO.output(11, True)

    return 'Door number 2 cycled'

run(host='0.0.0.0', port=1234)

# When on Raspberry Pi, create a new Python file with
# nano door.py
# Take script above and copy/paste it into that new Pi file
# Set up the file to boot with start up by adding
# nohup python /home/pi/garagedoor/door.py &
# Put that line into /etc/sc.local file in Pi
# I'll need to add some sort of security to it