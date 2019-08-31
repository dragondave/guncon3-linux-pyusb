import pyvjoy
from time import sleep

j = pyvjoy.VJoyDevice(1)

j.set_button(15,1) # turn button number 15 on
#Notice the args are (buttonID,state) whereas vJoy's native API is the other way around.

#turn button 15 off again
j.set_button(15,0)

#Set X axis to fully left
j.set_axis(pyvjoy.HID_USAGE_X, 0x1)

#Set X axis to fully right
j.set_axis(pyvjoy.HID_USAGE_X, 0x8000)

#Also implemented:

#j.reset()
#j.reset_buttons()
#j.reset_povs()


#The 'efficient' method as described in vJoy's docs - set multiple values at once

i=0
while True:
    i = i + 1
    sleep(.1)
    j.data.lButtons = i % 19 # buttons number 1,2 and 5 (1+2+16)
    j.data.wAxisX = 0x2000 + (i*100) % 2000
    j.data.wAxisY= 0x7500 - (i*100) % 2000

#send data to vJoy device
    j.update()
