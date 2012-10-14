'''
Created on Oct 14, 2012

@author: proteus
'''

import termios, sys, os
TERMIOS = termios
from vonProteus.RPi.BinTimer.BinTimer import BinTimer
import RPi.GPIO as GPIO
import time


GPIO.setmode(GPIO.BOARD)
LBut = 26;
RBut = 23;
TBut = 24;
GoBut = 22;

BUTTONDOWN = False;


GPIO.setup(LBut, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(RBut, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(TBut, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(GoBut, GPIO.IN, pull_up_down=GPIO.PUD_UP)

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
    
    while True:
        time.sleep(0.2)
#        x = getkey();
        
#        if x == 'a' : 
#            tmp.moveL()
#            break
#        if x ==  'd' : 
#            tmp.moveR()
#            break
#        if x ==  'w' : 
#            tmp.click()
#            break
#        if x == 's' : 
#            tmp.click()
#            break
#       
#        if x == 'g' :
#            tmp.go()
#            break

        if GPIO.input(LBut) == BUTTONDOWN : 
            tmp.moveL()
            tmp.migNow()
            break
        if GPIO.input(RBut) == BUTTONDOWN: 
            tmp.moveR()
            tmp.migNow()
            break
        if GPIO.input(TBut) == BUTTONDOWN: 
            tmp.click()
            time.sleep(0.5)
            break

        if GPIO.input(GoBut) == BUTTONDOWN:
            tmp.go()
            time.sleep(0.5)
            break
    
