#!/usr/bin/python

#Writes the temp data to a file

import time
import atexit

class WriteTemp:

	def __init__(self):
                self.f = open('TempData.txt','a')
		atexit.register(self.close)
		print("Initizled Write")
		

	def write(self,Temp, Humid):
		print("Write called: ",Temp, Humid)
		self.f.write(time.strftime("%a, %d %b %Y %H:%M:%S ", time.gmtime()))
		self.f.write('Tempature:')
		self.f.write(Temp)
		self.f.write(' Humidity:')
		self.f.write(Humid)
		self.f.write('\n')
		self.f.flush()
	
	def close(self):
		print("Closing stream")
		self.f.close()






if __name__ == "__main__":
	print "Testing write output"
	myWrite = WriteTemp()
	myWrite.write('10','20')
	myWrite.write('20','30')
	
