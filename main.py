from machine import Pin, Timer, PWM
import time


# globals
litLED = 5
setTime = 5
currentTime = 5
onBoardLed = Pin(25, Pin.OUT)
soundPin = Pin(18)
beepPWM = None
beepFreq = 500
beepDutyCycle = 32768

minCountdown = Timer()
blinkLed = Timer()
gymTimerPeriod = 3000 # one minute = 60000
blinkLedPeriod = 500

timerState = False


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
        

# start / stop timer function when gpio 22 is pressed
def startTimer(pin):
    global setTime
    global currentTime
    global minCountdown
    global blinkLed
    global timerState
    
    if timerState != True:  
        timerState = True
        print("Starting timer countdown from %d minutes..." % setTime)
        minCountdown.init(mode = Timer.PERIODIC, period = gymTimerPeriod, callback = countDown)
        blinkLed.init(mode = Timer.PERIODIC, period = blinkLedPeriod, callback = blinkingLed)
    else:
        print("Timer reset.")
        resetTimer()


# minCountDown timer callback function, counts down from setTime / currentTime
def countDown(pin):
    global currentTime
    global minCountdown
    global blinkLed
    
    currentTime -= 1
    
    if currentTime > 0:
        print("%d minutes left..." % currentTime)
        updateLeds()
    else:
        print("Times up!!")
        updateLeds()
        minCountdown.deinit()
        blinkLed.deinit()
        beepOn()
        time.sleep(2)
        beepOff()
        resetTimer()
        

# blinkLed timer callback function, blinks the onboard LED
def blinkingLed(pin):
    global onBoardLed
    
    onBoardLed.toggle()


# updates the LEDs to display the minutes remaining
def updateLeds():
    global currentTime
    
    for i in range(currentTime):
        Pin(i).value(1)
    
    for i in range(currentTime, 11):
        Pin(i).value(0)


# resets timer parameters
def resetTimer():
    global setTime
    global currentTime
    global onBoardLed
    global timerState
    global minCountdown
    global blinkLed
    
    setTime = 5
    currentTime = 5
    timerState = False
    minCountdown.deinit()
    blinkLed.deinit()
    # onBoardLed.value(0)
    updateLeds()
    

# turn on beepingPWM
def beepOn():
    global beepPWM
    global beepFreq
    global beepDutyCycle
    
    beepPWM = PWM(soundPin)
    beepPWM.freq(beepFreq)
    beepPWM.duty_u16(beepDutyCycle)


# turn off beepingPWM
def beepOff():
    global beepPWM
    
    beepPWM.deinit()


# running program

initLeds()
initButtons()

while True:
    pass