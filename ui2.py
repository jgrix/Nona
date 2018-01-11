import Tkinter as tk
import weather
from Tkinter import *
import thread
from time import sleep
import logData

BASE = RAISED
SELECTED = FLAT

# a base tab class
class Tab(Frame):
    def __init__(self, master, name):
        Frame.__init__(self, master)
        self.tab_name = name

# the bulk of the logic is in the actual tab bar
class TabBar(Frame):
    
	display_CT = None
	display_SetTemp = None
	display_Hum = None
	Mode = None
	weather_OT = None
	weather_Hum = None
	weather_High = None
	weather_Low = None
	weather_Wind = None
	setTemp = 60
	curTemp = None
	curHumid = None
	furnance_Firing = False


	def __init__(self, master=None, init_name=None, current_Temp = 9999, current_Humd=9999, furnanceFiring = False):
		Frame.__init__(self, master)
		self.tabs = {}
		self.buttons = {}
		self.current_tab = None
		self.init_name = init_name
		self.display_CT = tk.IntVar()
		self.display_SetTemp = tk.IntVar()
		self.display_Hum = tk.IntVar()
		self.Mode = tk.IntVar()
		self.weather_OT = tk.IntVar()
		self.weather_Hum = tk.IntVar()
		self.weather_High = tk.IntVar()
		self.weather_Low = tk.IntVar()
		self.weather_Wind = tk.StringVar()

		self.curTemp = current_Temp
		self.curHumid = current_Humd
		self.furnance_Firing = furnanceFiring

		self.display_CT.set(self.curTemp())
		self.display_Hum.set(self.curHumid())
		self.display_SetTemp.set(self.setTemp)


	def getMode(self):
		return self.Mode.get()

	def getSetTemp(self):
		return self.setTemp
        
	def show(self):
		self.pack(side=TOP, expand=YES, fill=X)
		self.switch_tab(self.init_name or self.tabs.keys()[-1])# switch the tab to the first tab
	
	def add(self, tab):
		tab.pack_forget()									# hide the tab on init
			
		self.tabs[tab.tab_name] = tab						# add it to the list of tabs
		b = Button(self, text=tab.tab_name, relief=BASE,	# basic button stuff
		command=(lambda name=tab.tab_name: self.switch_tab(name)))	# set the command to switch tabs
		b.pack(side=LEFT)												# pack the buttont to the left mose of self
		self.buttons[tab.tab_name] = b											# add it to the list of buttons
	
	def delete(self, tabname):
		
		if tabname == self.current_tab:
			self.current_tab = None
			self.tabs[tabname].pack_forget()
			del self.tabs[tabname]
			self.switch_tab(self.tabs.keys()[0])
            
		else: del self.tabs[tabname]
                
		self.buttons[tabname].pack_forget()
		del self.buttons[tabname]
                
                
	def switch_tab(self, name):
			if self.current_tab:
				self.buttons[self.current_tab].config(relief=BASE)
				self.tabs[self.current_tab].pack_forget()			# hide the current tab
			self.tabs[name].pack(side=BOTTOM)							# add the new tab to the display
			self.current_tab = name									# set the current tab to itself
			
			self.buttons[name].config(relief=SELECTED)					# set it to the selected style

	def update_W_Data(self):
		while (True):
			sleep(10)
			self.weather_OT.set(weather.outside_temp)
			self.weather_Hum.set(weather.get_Humidity())
			self.weather_High.set(weather.get_High())
			self.weather_Low.set(weather.get_Low())
			self.weather_Wind.set(weather.get_Wind())
			print "Weather:" + str(weather.outside_temp) + " " + str(weather.get_Humidity()) + " " + str(weather.get_High()) + " " + str(weather.get_Low()) + " " + str(weather.get_Wind())
			logData.logTemps(self.setTemp, self.curTemp(), weather.outside_temp, weather.get_High(), weather.get_Low(), weather.get_Humidity(), weather.get_Wind(), self.furnance_Firing(), self.getMode())

	pass

	def update_Display(self):
		while (True):
			sleep(1)
			self.display_CT.set(self.curTemp())
			self.display_Hum.set(self.curHumid())
			print str(self.curTemp()) + " "  + str(self.curHumid())

	def Increase_Tempature(self):
		self.setTemp += 1
		self.display_SetTemp.set(self.setTemp)
	pass

	def Decrease_Tempature(self):
		self.setTemp -= 1
		self.display_SetTemp.set(self.setTemp)
	pass


	def init_UI(self, root):
		thread.start_new_thread(weather.Update_Data, ())

		root.title("Thermostat")


		tab1 = Tab(root, "Tempature Control")                # notice how this one's master is the root instead of the bar
		#Label(tab1, text="Sunjay Varma is an extra ordinary little boy.\n\n\n\n\nCheck out his website:\nwww.sunjay-varma.com", bg="white", fg="red").pack(side=TOP, expand=YES, fill=BOTH)
		#Button(tab1, text="PRESS ME!", command=(lambda: write("YOU PRESSED ME!"))).pack(side=BOTTOM, fill=BOTH, expand=YES)
		#Button(tab1, text="KILL THIS TAB", command=(lambda: bar.delete("Wow..."))).pack(side=BOTTOM, fill=BOTH, expand=YES)

		#Button set up
		#display_CT.set(sTemp)
		frame_5 = Frame(tab1, height=3)
		frame_5.pack()
		button_Increase = tk.Button(frame_5, text = "++Increase", height = 3, width = 10, command = self.Increase_Tempature)
		button_Decrease = tk.Button(frame_5, text = "--Decrease", height = 3, width = 10, command = self.Decrease_Tempature)
		button_Increase.pack(side=LEFT)
		button_Decrease.pack(side=RIGHT)

		#Heating, Cooling, Off radio button
		frame_4 = Frame(tab1)
		frame_4.pack()
		Radiobutton(frame_4, text="Heating", variable=self.Mode, value = 1).pack(side = LEFT)
		Radiobutton(frame_4, text="Off", variable=self.Mode, value = 0).pack(side = LEFT)
		Radiobutton(frame_4, text="Cooling", variable=self.Mode, value = 2).pack(side = LEFT)
		Radiobutton(frame_4, text="Fan", variable=self.Mode, value = 3).pack(side = LEFT)
    
		#Set Tempature Display
		frame_1 = Frame(tab1)
		frame_1.pack()
		label_1 = tk.Label(frame_1, text="Hold tempature:")
		label_1.pack(side = LEFT)
		label_SetTemp = tk.Label(frame_1, textvariable=self.display_SetTemp, font=("Helvetica", 16), fg="orange")
		label_SetTemp.pack(side = RIGHT)
    
		#Current Tempature Display
		frame_2 = Frame(tab1)
		frame_2.pack()
		label_CT = tk.Label(frame_2, text="Current Temperature:")
		label_CT.pack(side=LEFT)
		Label_CT_Val = tk.Label(frame_2, textvariable=self.display_CT, font=("Helvetica", 16), fg="Green")
		Label_CT_Val.pack(side = RIGHT)
    
		#Current Humidity Display
		frame_3 = Frame(tab1)
		frame_3.pack()
		label_Hum = tk.Label(frame_3, text="Current Humidity:")
		label_Hum.pack(side=LEFT)
		Label_Hum_Val = tk.Label(frame_3, textvariable=self.display_Hum)
		Label_Hum_Val.pack(side = RIGHT)
    
    
    
    
		tab2 = Tab(root, "Outside Weather")
        #Label(tab2, text="How are you??", bg='black', fg='#3366ff').pack(side=TOP, fill=BOTH, expand=YES)
        #txt = Text(tab2, width=50, height=20)
        #txt.focus()
        #txt.pack(side=LEFT, fill=X, expand=YES)
        #Button(tab2, text="Get", command=(lambda: write(txt.get('1.0', END).strip()))).pack(side=BOTTOM, expand=YES, fill=BOTH)
		self.weather_OT.set(weather.outside_temp)
		self.weather_Hum.set(weather.get_Humidity())
		self.weather_High.set(weather.get_High())
		self.weather_Low.set(weather.get_Low())
		self.weather_Wind.set(weather.get_Wind())
    
		frame_weather_1 = Frame(tab2)
		frame_weather_1.pack()
		Label(frame_weather_1, text="Outside Tempature:").pack(side = LEFT)
		Label(frame_weather_1, textvariable=self.weather_OT , font=("Helvetica", 16), fg="Green").pack(side = RIGHT)
    
		frame_weather_2 = Frame(tab2)
		frame_weather_2.pack()
		Label(frame_weather_2, text="Relative Humidity:").pack(side = LEFT)
		Label(frame_weather_2, textvariable=self.weather_Hum , font=("Helvetica", 16), fg="Green").pack(side = RIGHT)
    
		frame_weather_3 = Frame(tab2)
		frame_weather_3.pack()
		Label(frame_weather_3, text="High:").pack(side = LEFT)
		Label(frame_weather_3, textvariable=self.weather_High , font=("Helvetica", 16), fg="Green").pack(side = RIGHT)
    
		frame_weather_4 = Frame(tab2)
		frame_weather_4.pack()
		Label(frame_weather_4, text="Low:").pack(side = LEFT)
		Label(frame_weather_4, textvariable=self.weather_Low , font=("Helvetica", 16), fg="Green").pack(side = RIGHT)
    
		frame_weather_5 = Frame(tab2)
		frame_weather_5.pack()
		Label(frame_weather_5, text="Wind:").pack(side = LEFT)
		Label(frame_weather_5, textvariable=self.weather_Wind , font=("Helvetica", 16), fg="Green").pack(side = RIGHT)
    
    
    
		tab3 = Tab(root, "Info")
		Label(tab3, bg='white', text="Place holder. Should this be for cost estimates?").pack(side=LEFT, expand=YES, fill=BOTH)
    
		self.add(tab1)                   # add the tabs to the tab bar
		self.add(tab2)
		self.add(tab3)
    
        #bar.config(bd=2, relief=RIDGE)            # add some border
    
		thread.start_new_thread(self.update_W_Data, ())
		thread.start_new_thread(self.update_Display, ())
    
		self.show()

if __name__ == '__main__':
    root1 = tk.Tk()
    bar = TabBar(root1, "Tempature Control")
    bar.init_UI(root1)
    root1.mainloop()
