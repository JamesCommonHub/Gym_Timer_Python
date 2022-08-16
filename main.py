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



while True:
    pass