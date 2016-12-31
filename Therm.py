#!/usr/bin/python

import sys
import Tkinter
import DHT22
import pigpio
import thread
import CtoF
import Relay_Fire
import WriteTempData
import atexit
#import TCPServer
import RPi.GPIO as GPIO
import atexit

from time import sleep
from Tkinter import *

Set_Temp = 60
Current_Temp = 60
input_Temp_Up = 17
input_Temp_Down = 22

GPIO.setup(input_Temp_Up, GPIO.IN)
GPIO.setup(input_Temp_Down, GPIO.IN)

top = Tkinter.Tk()
display_var = Tkinter.IntVar()
display_CT = Tkinter.IntVar()
display_Hum = Tkinter.IntVar()
Mode = Tkinter.IntVar()


def read_Current_Tempature():
	"Reads the current Tempature"
        global Current_Temp
	pi = pigpio.pi()
	sensor = DHT22.sensor(pi, 4, LED=16, power=8)
	myWrite = WriteTempData.WriteTemp()

	while True:
		sleep(0.2)
		sensor.trigger()
		faren = sensor.temperature()
		faren = CtoF.C_to_F(faren)
		Current_Temp = faren
		print("Current Temp:",faren)
		display_CT.set('{:.4}'.format(float(faren)))
		myHum = sensor.humidity()
		print("Humidity is:",myHum)
		display_Hum.set('{:.4}'.format(float(myHum)))
		myWrite.write(str(Current_Temp), str(myHum))
		sleep(3)

	sensor.cancel()
	pi.stop()
pass

def watch_For_Input_Pins():
	"Watches for the inputs on the LCD panel"
#	global Set_Temp
	global input_Temp_Up
	global input_Temp_Down

	while 1:
		#sleep(1)
		#print("Watching for input")
		if GPIO.input(input_Temp_Up):
			Set_Temp+=1
			print("Button press increase temp")
		if GPIO.input(input_Temp_Down):
			Set_Temp-=1
			print("Button press decrese temp")
	


pass

def fire_Furn():
	#global Mode
	#global Current_Temp
	#global Set_Temp
	recent_act = False
	sleep(8) #Sensor Lag	

	while True:
		mode = Mode.get()
		#print("Entering top of loop", mode, Current_Temp)
		sleep(5)
		if mode == 0: #Off	
			#print("Off")		
			Relay_Fire.All_Off()
		if mode == 1: #Heating
			print("Heating")
			if int(Current_Temp) < int(Set_Temp):
				print("Fire heat on")				
				Relay_Fire.Heat_On()
			elif int(Current_Temp) > int(Set_Temp):
				print("Fire heat off")
				Relay_Fire.All_Off()
			else:
				print("Heating no action")
			
		if mode == 2: #Cooling
			#print("Cooling")
			if int(Current_Temp) > int(Set_Temp):
				Relay_Fire.Cool_On()
			elif int(Current_Temp) < int(Set_Temp):
				Relay_Fire.All_Off()

		
	
pass

def close():
	Relay_Fire.All_Off()
		

def increase_tempature():
    "Increases the stored tempature"
    global Set_Temp
#    print('Tempature was:', Set_Temp)
    Set_Temp += 1
    display_var.set(Set_Temp)
#    print('Tempature increased to:', Set_Temp)
pass

def decrease_tempature():
    "Decreases the stored tempature"
    global Set_Temp
#    print('Tempature was:', Set_Temp)
    Set_Temp -= 1
    display_var.set(Set_Temp)
#    print('Tempature decreased to:', Set_Temp)
pass

def Set_Target_temp(target):
	global Set_Temp
	Set_Temp = target
	display_var.set(Set_Temp)

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
	#Button set up
	display_var.set(Set_Temp)
	frame_5 = Frame(top)
	frame_5.pack()
	button_Increase = Tkinter.Button(frame_5, text = "++Increase", command = increase_tempature, height = 4, width = 15)
	button_Decrease = Tkinter.Button(frame_5, text = "--Decrease", command = decrease_tempature, height = 4, width = 15)
	button_Increase.pack(side=LEFT)
	button_Decrease.pack(side=RIGHT)

	#Heating, Cooling, Off radio button
	frame_4 = Frame(top)
	frame_4.pack()
	Radiobutton(frame_4, text="Heating", variable=Mode, value = 1).pack(side = LEFT)
	Radiobutton(frame_4, text="Off", variable=Mode, value = 0).pack(side = LEFT)
	Radiobutton(frame_4, text="Cooling", variable=Mode, value = 2).pack(side = LEFT)

	#Set Tempature Display
	frame_1 = Frame(top)
	frame_1.pack()
	label_1 = Tkinter.Label(frame_1, text="Hold tempature:")
	label_1.pack(side = LEFT)
	label_SetTemp = Tkinter.Label(frame_1, textvariable=display_var, font=("Helvetica", 16), fg="orange")
	label_SetTemp.pack(side = RIGHT)

	#Current Tempature Display
	frame_2 = Frame(top)
	frame_2.pack()
	label_CT = Tkinter.Label(frame_2, text="Current Temperature:")
	label_CT.pack(side=LEFT)
	Label_CT_Val = Tkinter.Label(frame_2, textvariable=display_CT, font=("Helvetica", 16), fg="Green")
	Label_CT_Val.pack(side = RIGHT)

	#Current Humidity Display
	frame_3 = Frame(top)
	frame_3.pack()
	label_Hum = Tkinter.Label(frame_3, text="Current Humidity:")
	label_Hum.pack(side=LEFT)
	Label_Hum_Val = Tkinter.Label(frame_3, textvariable=display_Hum)
	Label_Hum_Val.pack(side = RIGHT)

	thread.start_new_thread(read_Current_Tempature, ())
	thread.start_new_thread(fire_Furn, ())
#	thread.start_new_thread(watch_For_Input_Pins, ())
	
	atexit.register(close)

#   	myComm = TCPServer.Andriod_Comms(Comms_Callback)
#	myComm.start()




	top.mainloop()
