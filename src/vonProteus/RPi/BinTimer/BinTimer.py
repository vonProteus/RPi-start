'''
Created on Oct 14, 2012

@author: proteus
'''
from array import array
import time
import RPi.GPIO as GPIO




class BinTimer(object):
    '''
    classdocs
    '''


    def __init__(self):
        '''
        Constructor
        '''
        print "init start"
        self.leds = {'gpio': array('i',[5,7,10,8,11,12]),'led': array('i',[0,0,0,0,0,0]), 'now': 0, 'val': 0, 'statLed':21}
        GPIO.setmode(GPIO.BOARD)
        GPIO.setup(self.leds['statLed'], GPIO.OUT)
        GPIO.output(self.leds['statLed'],1)
     
    def setup(self):
        print "setup"
    
    def moveR(self):
        print "moveR"
        if self.leds['now'] >0 :
            self.leds['now'] -= 1;
#        print "now " + str(self.leds['now'])
        
    def moveL(self):
        print "moveL"
        if self.leds['now'] < 5 :
            self.leds['now'] += 1;
#        print "now " + str(self.leds['now'])
        
    def updateDisplay(self):
        print "update Display"
        GPIO.setmode(GPIO.BOARD)
        
        line0 = "";
        line1 = "";
        line2 = "";
        for a in range(5,-1,-1):
            if a == self.leds['now']:
                line0 += " *";
            else :
                line0 += " " + str(a)
                
            line1 += " " + str(self.leds['gpio'][a])
            line2 += " " + str(self.leds['led'][a])
            GPIO.setup(self.leds['gpio'][a], GPIO.OUT)
            GPIO.output(self.leds['gpio'][a],self.leds['led'][a])
        print line0;
        print line1;
        print line2;
        print "val = " + str(self.leds['val'])
        print "now = " + str(self.leds['now'])
        
    def click(self):
        print "click"
        if int(self.leds['led'][self.leds['now']]):
            self.clickOff();
            self.leds['val'] -= pow(2, self.leds['now'])
        else:
            self.clickOn();
            self.leds['val'] += pow(2, self.leds['now'])
#        print "teraz " + str(self.leds['led'][self.leds['now']])
        
    def clickOn(self):
        self.leds['led'][self.leds['now']] = 1;
        
    def clickOff(self):
        self.leds['led'][self.leds['now']] = 0;
        
    def go(self):
        if self.leds['val'] >= 2 :
            self.goStart()
            print "go"
            
            while self.leds['val'] > 0 :
                self.updateDisplay();
                self.leds['val'] -= 1
                binStr = str(bin(self.leds['val']))
                binStr = binStr.replace("0b", "")
                
                for a in range(5,-1,-1):
                    self.leds['led'][a] = 0;
                b = 0;
                for a in range(len(binStr)-1,-1,-1):
                    self.leds['led'][a] = int(binStr[b])
                    b += 1;
                time.sleep(1)

            
            self.goStop()
        else:
            print "za maly val"
            
    def goStart(self):
        print "lampka off"
        GPIO.setmode(GPIO.BOARD)
        GPIO.setup(self.leds['statLed'], GPIO.OUT)
        GPIO.output(self.leds['statLed'],0)
        
    def goStop(self):
        print "lampka on + miganie czy cus"
        GPIO.setmode(GPIO.BOARD)
        GPIO.setup(self.leds['statLed'], GPIO.OUT)
        for a in range(5,-1,-1):
            GPIO.setup(self.leds['gpio'][a], GPIO.OUT)
        mig = 1
        for a in range(0,3) :
            time.sleep(0.3)
            GPIO.output(self.leds['statLed'], mig)
            for a in range(5,-1,-1):
                time.sleep(0.5)
                GPIO.output(self.leds['gpio'][a],mig)
            if mig == 1 :
                mig = 0;
            else:
                mig = 1;
        
        GPIO.cleanup()
        exit(0)
        