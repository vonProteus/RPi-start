'''
Created on Oct 14, 2012

@author: proteus
'''

import termios, sys, os
TERMIOS = termios
from vonProteus.RPi.BinTimer.BinTimer import BinTimer
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BOARD)

def getkey():
    fd = sys.stdin.fileno()
    old = termios.tcgetattr(fd)
    new = termios.tcgetattr(fd)
    new[3] = new[3] & ~TERMIOS.ICANON & ~TERMIOS.ECHO
    new[6][TERMIOS.VMIN] = 1
    new[6][TERMIOS.VTIME] = 0
    termios.tcsetattr(fd, TERMIOS.TCSANOW, new)
    c = None
    try:
        c = os.read(fd, 1)
    finally:
        termios.tcsetattr(fd, TERMIOS.TCSAFLUSH, old)
    return c


    
    


if __name__ == '__main__':
    pass

print "test "; 

tmp = BinTimer();


while True :
    tmp.updateDisplay();
    
    x = getkey();
    if x == 'a' : 
        tmp.moveL()
    if x ==  'd' : 
        tmp.moveR()
    if x ==  'w' : 
        tmp.click()
    if x == 's' : 
        tmp.click()
   
    if x == 'g' :
        tmp.go()
        
    
