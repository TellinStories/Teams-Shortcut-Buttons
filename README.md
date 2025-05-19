I spend a lot of my work day in Teams meetings and frequently need to mute / unmute my microphone, turn my camera on and off, or raise or lower my hand.  
If using my mouse I invariably can’t find the right icon to click fast enough and I never remember the right keyboard shortcuts.  
So I built a  simple device so that I can press one big fat arcade button for each of those actions.
The device is simple – three arcade buttons which are connected to an RP2040 Zero microcontroller.  
I chose the RP2040 because it is cheap, very small and I am already used to using Raspberry Pi Picos (which would also work well); other microcontrollers may also be suitable but I am not experienced in using them.
The microcontroller runs a simple programme that sends the keyboard shortcuts to your computer when a button is pressed, as if it were a keyboard.  
For example, if you press the microphone mute / unmute button then “CTRL+SHIFT+M” is sent to your computer which is the mute / unmute shortcut.  
Each button press toggles the LED built into the arcade button between on and off.  
