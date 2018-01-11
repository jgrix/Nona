import RPi.GPIO as GPIO
import time

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM) # Broadcom pin-numbering scheme
HEAT = 3
COOL = 5
FAN = 6
POWER = 2

GPIO.setup(HEAT, GPIO.OUT) 
GPIO.setup(COOL, GPIO.OUT)
GPIO.setup(FAN, GPIO.OUT)
GPIO.setup(POWER, GPIO.OUT)

def Init_Power():
	GPIO.output(POWER, GPIO.LOW)
pass

def Exit_Power():
	GPIO.output(POWER, GPIO.HIGH)
pass	

def Heat_On():
	GPIO.output(HEAT, GPIO.LOW)
    GPIO.output(COOL, GPIO.HIGH)
	GPIO.output(FAN, GPIO.HIGH)
	#print("Firing Heat")
pass

def Heat_Off():
        GPIO.output(HEAT, GPIO.HIGH)
pass

def Cool_On():
	GPIO.output(COOL, GPIO.LOW)
    GPIO.output(HEAT, GPIO.HIGH)
	GPIO.output(FAN, GPIO.HIGH)
	#print("Firing Cool")
pass

def Cool_Off():
	GPIO.output(COOL, GPIO.HIGH)
pass

def Fan_ON():
    GPIO.output(FAN, GPIO.LOW)
    GPIO.output(HEAT, GPIO.HIGH)
	GPIO.output(COOL, GPIO.HIGH)

def All_Off():
	GPIO.output(HEAT, GPIO.HIGH)
	GPIO.output(COOL, GPIO.HIGH)
	GPIO.output(FAN, GPIO.HIGH)
	#print("All Off")
pass

	

#GPIO.output(18, GPIO.LOW)
#GPIO.output(23, GPIO.LOW)

if __name__ == "__main__":
	print("Running Test")

	All_Off()
	time.sleep(3)
	Heat_On()
	time.sleep(3)
	Cool_On()
	time.sleep(3)
	All_Off()
