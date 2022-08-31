# Gym_Timer_Python

Raspberry Pi Pico DIY gym timer using Micro Python.  Code is written to work with the Pico along side feature-packed Maker board.

![Maker Pi Pico Diagram](hhttps://github.com/JamesCommonHub/Gym_Timer_Python/blob/main/img/MakerPiPicoDiagram.png)


## Instructions

On boot up, timer will default to 5 minutes.

* Pressing GPIO 20 adds a minute to the timer, up to a maximum of 10 minutes.
* Pressing GPIO 21 subtracts a minute from the timer, to a minimum of 1 minute.
* Pressing GPIO 22 starts the timer.  If it is pressed again while the timer is running, will stop and reset the timer back to its default.

If minutes are added or subtracted while the timer is running, timer will restart and countdown from the new time set.