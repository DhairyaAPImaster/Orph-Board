from machine import Pin
import time

LED = Pin(15, Pin.OUT)

while True:
    LED.on()
    time.sleep(0.5)

    LED.off()
    time.sleep(0.5)