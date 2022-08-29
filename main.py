from machine import Pin, Timer, PWM
import time


# globals
litLED = 5
setTime = 5
currentTime = 5
onBoardLed = Pin(25, Pin.OUT)


# timer object
minCountdown = Timer()
ledBlink = Timer()


# initializes LED gpios 0-9
def initLeds():
    
    for i in range(10):
        Pin(i, Pin.OUT)


# initializes interrupts to gpios 20-22
def initButtons():
    p20 = Pin(20, Pin.IN, Pin.PULL_UP)
    p20.irq(addOne, Pin.IRQ_FALLING)

    p21 = Pin(21, Pin.IN, Pin.PULL_UP)
    p21.irq(subOne, Pin.IRQ_FALLING)

    p22 = Pin(22, Pin.IN, Pin.PULL_UP)
    p22.irq(startTimer, Pin.IRQ_FALLING)


# adds a minute to setTime & currentTime when gpio 20 is pressed
def addOne(pin):
    global setTime
    global currentTime
    
    if setTime < 10:
        setTime += 1
        currentTime = setTime
        print("Timer set for %d minutes." % setTime)
        updateLeds()
    else:
        setTime = 10
        currentTime = setTime
        print("Timer set for %d minutes." % setTime)
        updateLeds()
    

# adds a minute to setTime & currentTime when gpio 21 is pressed
def subOne(pin):
    global setTime
    global currentTime
    
    if setTime > 1:
        setTime -= 1
        currentTime = setTime
        print("Timer set for %d minutes." % setTime)
        updateLeds()
    else:
        setTime = 1
        currentTime = setTime
        print("Timer set for %d minutes." % setTime)
        updateLeds()

# running program

initLeds()
initButtons()

while True:
    pass