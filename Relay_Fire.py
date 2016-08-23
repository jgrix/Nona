import RPi.GPIO as GPIO
import time

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM) # Broadcom pin-numbering scheme
GPIO.setup(14, GPIO.OUT) 
GPIO.setup(15, GPIO.OUT)
GPIO.setup(18, GPIO.OUT)
GPIO.setup(23, GPIO.OUT)

def Heat_On():
	GPIO.output(14, GPIO.LOW)
        GPIO.output(15, GPIO.HIGH)
	#print("Firing Heat")
pass

def Heat_Off():
        GPIO.output(14, GPIO.HIGH)
pass

def Cool_On():
	GPIO.output(15, GPIO.LOW)
        GPIO.output(14, GPIO.HIGH)
	#print("Firing Cool")
pass

def Cool_Off():
	GPIO.output(15, GPIO.HIGH)
pass

def All_Off():
	GPIO.output(14, GPIO.HIGH)
	GPIO.output(15, GPIO.HIGH)
	GPIO.output(18, GPIO.HIGH)
	GPIO.output(23, GPIO.HIGH)
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
