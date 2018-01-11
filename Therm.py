#!/usr/bin/python

####CHange to true for when running on the Raspberry Pi
runningOnTarget = False
########################

import sys
import Tkinter
if runningOnTarget:
    import DHT22
    import RPi.GPIO as GPIO
    import pigpio
    import Relay_Fire
import thread
import CtoF
import atexit
#import UI
import ui2
#import TCPServer

import atexit

from time import sleep
from Tkinter import *

current_Temp = 60
current_Humd = 50

furnace_Firing = False



input_Temp_Up = 17
input_Temp_Down = 22

if runningOnTarget : GPIO.setup(input_Temp_Up, GPIO.IN)
if runningOnTarget : GPIO.setup(input_Temp_Down, GPIO.IN)



def Read_current_Tempature():
	"Reads the current Tempature"
	global current_Temp
	pi = pigpio.pi()
	sensor = DHT22.sensor(pi, 4, LED=16, power=8)

	while True:
		sleep(0.2)
		sensor.trigger()
		faren = sensor.temperature()
		faren = CtoF.C_to_F(faren)
		current_Temp = faren
		print("Current Temp:",faren)
        #display_CT.set('{:.4}'.format(float(faren)))
		myHum = sensor.humidity()
		print("Humidity is:",myHum)
        current_Humd = muHum
        #display_Hum.set('{:.4}'.format(float(myHum)))
        sleep(3)

	sensor.cancel()
	pi.stop()
pass

def Watch_For_Input_Pins():
	"Watches for the inputs on the LCD panel"
#	global set_Temp
	global input_Temp_Up
	global input_Temp_Down

	while 1:
		#sleep(1)
		#print("Watching for input")
		if GPIO.input(input_Temp_Up):
		        set_Temp+=1
			print("Button press increase temp")
		if GPIO.input(input_Temp_Down):
		        set_Temp-=1
			print("Button press decrese temp")

pass

def Fire_Furn(SETTEMP, MODE):
	global furnace_Firing
	
	sleep(8) #Sensor Lag
	
	while True:
		mode = MODE()
		seTemp = SETTEMP
		#print("Entering top of loop", mode, current_Temp)
		sleep(5)
		if mode == 0: #Off
			furnace_Firing = False
			Relay_Fire.All_Off()

		if mode == 1: #Heating
			if int(current_Temp) < int(setTemp):
				furnace_Firing = True
				Relay_Fire.Heat_On()
		elif int(current_Temp) > int(seTemp):

			furnace_Firing = False
			Relay_Fire.All_Off()

		if mode == 2: #Cooling
			if int(current_Temp) > int(setTemp):
				Relay_Fire.Cool_On()
				furnace_Firing = True
			elif int(current_Temp) < int(setTemp):
				Relay_Fire.All_Off()
				furnace_Firing = False

		if mode == 3: #Fan
			Relay_Fire.Fan_ON()


		
	
pass

def test_Temp(SETTEMP, MODE):
    global current_Temp
    global current_Humd
	
    while True:
		mode = MODE()
		seTemp = SETTEMP()
		sleep(2)
		current_Temp+=1
		current_Humd+=1
		print "temp: " + str(current_Temp) + " Hum " + str(current_Humd) + " Set Temp " + str(seTemp) + " Mode " + str(mode)


def Close():
	Relay_Fire.All_Off()

def getTemp():
    global current_Temp
    return current_Temp

def getHumd():
    global current_Humd
    return current_Humd

def getFurnanceFiring():
	global furnace_Firing
	return furnace_Firing

if __name__ == "__main__":
    top = Tkinter.Tk()
    bar = ui2.TabBar(top, "Tempature Control", getTemp, getHumd, getFurnanceFiring)
    bar.init_UI(top)
	
	
    
    
    if runningOnTarget :
        thread.start_new_thread(Read_current_Tempature, ())
        thread.start_new_thread(Fire_Furn, (bar.getSetTemp, bar.getMode))
        Relay_Fire.Init_Power() #Fires our relay diverting power from the back up thermostat
        atexit.register(Relay_Fire.Exit_Power)
        atexit.register(Close)
    else:
        thread.start_new_thread(test_Temp,(bar.getSetTemp, bar.getMode))

        
    top.mainloop()
