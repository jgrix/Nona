#!/usr/bin/python

import sys
import DHT22
import pigpio
import thread
import CtoF
import Relay_Fire
import WriteTempData
import atexit
import UI_Qt as UI
#import TCPServer
import RPi.GPIO as GPIO
import atexit

from time import sleep

set_Temp = 60
current_Temp = 60
input_Temp_Up = 17
input_Temp_Down = 22
display_var = 0
display_CT = 0
display_Hum = 0
mode = 0

GPIO.setup(input_Temp_Up, GPIO.IN)
GPIO.setup(input_Temp_Down, GPIO.IN)




def Read_current_Tempature():
	"Reads the current Tempature"
        global current_Temp, display_CT, display_HUM

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
		display_CT.set('{:.4}'.format(float(faren)))
		myHum = sensor.humidity()
		print("Humidity is:",myHum)
		display_Hum.set('{:.4}'.format(float(myHum)))
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

def Fire_Furn():
	recent_act = False
	sleep(8) #Sensor Lag	

	while True:	       
		#print("Entering top of loop", mode, current_Temp)
		sleep(5)
		if mode == 0: #Off
			#print("Off")		
			Relay_Fire.All_Off()
		if mode == 1: #Heating
			print("Heating")
			if int(current_Temp) < int(set_Temp):
				print("Fire heat on")				
				Relay_Fire.Heat_On()
			elif int(current_Temp) > int(set_Temp):
				print("Fire heat off")
				Relay_Fire.All_Off()
			else:
				print("Heating no action")
			
		if mode == 2: #Cooling
			#print("Cooling")
			if int(current_Temp) > int(set_Temp):
				Relay_Fire.Cool_On()
			elif int(current_Temp) < int(set_Temp):
				Relay_Fire.All_Off()

		
	
pass

def Close():
	Relay_Fire.All_Off()
		

def Increase_Tempature():
    "Increases the stored tempature"
    global set_Temp
#    print('Tempature was:', set_Temp)
    set_Temp += 1
    display_var.set(set_Temp)
#    print('Tempature increased to:', set_Temp)
pass

def Decrease_Tempature():
    "Decreases the stored tempature"
    global set_Temp
#    print('Tempature was:', set_Temp)
    set_Temp -= 1
    display_var.set(set_Temp)
#    print('Tempature decreased to:', set_Temp)
pass

def Set_Target_temp(target):
        global set_Temp
        set_Temp = target
        display_var.set(set_Temp)

def Comms_Callback(arg1):
	print("Message Received:", arg1)

	if "Set Target Temp:" in arg1:
		val = arg1.replace("Set Target Temp:","")
		print("Setting the target temp to:",val)
		Set_Target_temp(float(val))



if __name__ == "__main__":
	global data
	Relay_Fire.Init_Power() #Fires our relay diverting power from the back up thermostat
	atexit.register(Relay_Fire.Exit_Power)

        UI.Setup_UI(Increase_Tempature, Decrease_Tempature, set_Temp, current_Temp)

        thread.start_new_thread(Read_current_Tempature, ())
        thread.start_new_thread(Fire_Furn, ())
        atexit.register(Close)




