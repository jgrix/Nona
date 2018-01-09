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
import WriteTempData
import atexit
#import UI
import ui2
#import TCPServer

import atexit

from time import sleep
from Tkinter import *

current_Temp = 60
current_Humd = 50
input_Temp_Up = 17
input_Temp_Down = 22

if runningOnTarget : GPIO.setup(input_Temp_Up, GPIO.IN)
if runningOnTarget : GPIO.setup(input_Temp_Down, GPIO.IN)



def Read_current_Tempature():
	"Reads the current Tempature"
	global current_Temp
	pi = pigpio.pi()
	sensor = DHT22.sensor(pi, 4, LED=16, power=8)
	myWrite = WriteTempData.WriteTemp()

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
		myWrite.write(str(current_Temp), str(myHum))
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

def Fire_Furn(setTemp, mode):
        #global mode
        #global current_Temp
        #global set_Temp
	recent_act = False
	sleep(8) #Sensor Lag	

	while True:
	        mode = mode.get()
		#print("Entering top of loop", mode, current_Temp)
		sleep(5)
		if mode == 0: #Off
			#print("Off")		
			Relay_Fire.All_Off()
		if mode == 1: #Heating
			print("Heating")
			if int(current_Temp) < int(setTemp):
				print("Fire heat on")				
				Relay_Fire.Heat_On()
			elif int(current_Temp) > int(seTemp):
				print("Fire heat off")
				Relay_Fire.All_Off()
			else:
				print("Heating no action")
			
		if mode == 2: #Cooling
			#print("Cooling")
			if int(current_Temp) > int(setTemp):
				Relay_Fire.Cool_On()
			elif int(current_Temp) < int(setTemp):
				Relay_Fire.All_Off()

		
	
pass

def Close():
	Relay_Fire.All_Off()


if __name__ == "__main__":
    top = Tkinter.Tk()
    bar = ui2.TabBar(top, "Tempature Control")
    bar.init_UI(top)
    
    
    if runningOnTarget :
        thread.start_new_thread(Read_current_Tempature, ())
        thread.start_new_thread(Fire_Furn, (bar.setTemp, bar.Mode))
        Relay_Fire.Init_Power() #Fires our relay diverting power from the back up thermostat
        atexit.register(Relay_Fire.Exit_Power)
        atexit.register(Close)

        
    top.mainloop()
