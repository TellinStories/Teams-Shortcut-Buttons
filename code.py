# Imports
import board
import digitalio
import usb_hid
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keycode import Keycode
import time

# Constants
DEBOUNCE_TIME = 0.1  # Debounce time set at this number of seconds
STARTUP_BLINK_TIME = 0.2  # The LEDs blink at start up for this number of seconds

# Setting up the buttons
# Button 1 (Hand) on GPIO14
button1 = digitalio.DigitalInOut(board.GP14)
button1.direction = digitalio.Direction.INPUT
button1.pull = digitalio.Pull.UP  # Pull Ups as button connects to GND when pressed

# Button 2 (Camera) on GPIO26
button2 = digitalio.DigitalInOut(board.GP26)
button2.direction = digitalio.Direction.INPUT
button2.pull = digitalio.Pull.UP  

# Button 3 (Microphone) on GPIO28
button3 = digitalio.DigitalInOut(board.GP28)
button3.direction = digitalio.Direction.INPUT
button3.pull = digitalio.Pull.UP  

# Setting up the LEDs
# Button 1 (Hand) LED - LED1 on GPIO15
led1 = digitalio.DigitalInOut(board.GP15)
led1.direction = digitalio.Direction.OUTPUT
led1.value = False  # Sets the LED to off 

# Button 2 (Camera) LED - LED2 on GPIO27
led2 = digitalio.DigitalInOut(board.GP27)
led2.direction = digitalio.Direction.OUTPUT
led2.value = False  # Sets the LED to off

# Button 3's LED - LED2 on GPIO29
led3 = digitalio.DigitalInOut(board.GP29)
led3.direction = digitalio.Direction.OUTPUT
led3.value = False  # Sets the LED to off

# Set up the keyboard
keyboard = Keyboard(usb_hid.devices)

# This makes the LEDs blink at start up
for _ in range(3):
    led1.value = True
    led2.value = True
    led3.value = True
    time.sleep(STARTUP_BLINK_TIME)
    led1.value = False
    led2.value = False
    led3.value = False 
    time.sleep(STARTUP_BLINK_TIME)

while True:
    if button1.value is False:  # Button pressed (active low)
        led1.value = not led1.value  # This toggles the LED on / off
        keyboard.press(Keycode.CONTROL, Keycode.SHIFT, Keycode.K) # Mimics pressing CTRL+SHIFT+K
        print("Raise / Lower Hand button pressed")
        time.sleep(DEBOUNCE_TIME)  # Debounce
        keyboard.release_all()  # Release all keys
        while button1.value is False:
            time.sleep(0.01)

    if button2.value is False:  # Button pressed (active low)
        led2.value = not led2.value  # This toggles the LED on / off
        keyboard.press(Keycode.CONTROL, Keycode.SHIFT, Keycode.O) # Mimics pressing CTRL+SHIFT+O
        print("Camera on/off button pressed")
        time.sleep(DEBOUNCE_TIME)  # Debounce
        keyboard.release_all()  # Release all keys
        while button2.value is False:
            time.sleep(0.01)

    if button3.value is False:  # Button pressed (active low)
        led3.value = not led3.value  # This toggles the LED on / off
        keyboard.press(Keycode.CONTROL, Keycode.SHIFT, Keycode.M) # Mimics pressing CTRL+SHIFT+M
        print("Mute / Unmute button pressed")
        time.sleep(DEBOUNCE_TIME)  # Debounce
        keyboard.release_all()  # Release all keys
        while button3.value is False:
            time.sleep(0.01)

    time.sleep(0.01)  # Delay
