I spend a lot of my work day in Teams meetings and frequently need to mute / unmute my microphone, turn my camera on and off, or raise or lower my hand.  
If using my mouse I invariably can’t find the right icon to click fast enough and I never remember the right keyboard shortcuts. 
So I built a  simple device so that I can press one big fat arcade button for each of those actions.
![IMG_7282](https://github.com/user-attachments/assets/e70f9911-f114-4600-92f9-e8fb5044c0d4)


The device is simple – three arcade buttons which are connected to an RP2040 Zero microcontroller.  
I chose the RP2040 because it is cheap, very small and I am already used to using Raspberry Pi Picos (which would also work well); other microcontrollers may also be suitable but I am not experienced in using them.
The microcontroller runs a simple programme that sends the keyboard shortcuts to your computer when a button is pressed, as if it were a keyboard.  
For example, if you press the microphone mute / unmute button then “CTRL+SHIFT+M” is sent to your computer which is the mute / unmute shortcut.  
Each button press toggles the LED built into the arcade button between on and off.  

The programme is written in Circuit Python and requires the Adafruit HID Library https://docs.circuitpython.org/projects/hid/en/latest/index.html and https://github.com/adafruit/Adafruit_CircuitPython_Bundle  
You need to copy the library files from the the Adafruit HID Library to your RP2040 / Raspberry Pi Pico library folder and then copy the code.py file from this GitHub.

Full instructions are in the Teams Buttins Instructions PDF file.

I took inspiration from this project: https://github.com/ttan/Mute-o-Matic-V2 - thank you to the author.
