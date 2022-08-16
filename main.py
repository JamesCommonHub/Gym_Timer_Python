from machine import Pin, Timer, PWM


# global variables
litLED = 5
setTime = 5

# timer object
minCountdown = Timer()
ledBlink = Timer()

# initializes LED gpios 0-9
def initLeds():
    
    for i in range(10):
        Pin(i, Pin.OUT)
        # print(i)
        
    for i in range(litLED):
        Pin(i).value(1)

# initializes interrupts to gpios 20-22
def initButtons():
    p20 = Pin(20, Pin.IN, Pin.PULL_UP)
    p20.irq(lambda pin: print("GP20 has been pressed"), Pin.IRQ_FALLING)

    p21 = Pin(21, Pin.IN, Pin.PULL_UP)
    p21.irq(lambda pin: print("GP21 has been pressed"), Pin.IRQ_FALLING)

    p22 = Pin(22, Pin.IN, Pin.PULL_UP)
    # p22.irq(lambda pin: print("GP22 has been pressed"), Pin.IRQ_FALLING)
    p22.irq(countDown, Pin.IRQ_FALLING)


while True:
    pass