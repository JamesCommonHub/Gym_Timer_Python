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


# running program

initLeds()
initButtons()

while True:
    pass