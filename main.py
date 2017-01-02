import gopigo
import sys
import time

#import atexit
#atexit.register(stop)

while 1:
    gopigo.led_on(0)
    print ("LED turned off")
    time.sleep(0.5)
    gopigo.led_on(1)
    print ("LED turned on")
    time.sleep(0.5)

