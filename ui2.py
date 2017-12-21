import Tkinter as tk
import weather
from Tkinter import *
import thread
from time import sleep

root = tk.Tk()
display_CT = tk.IntVar()
display_HT = tk.IntVar()
display_Hum = tk.IntVar()
Mode = tk.IntVar()
weather_OT = tk.IntVar()

setTemp = 60
curTemp = 60

BASE = RAISED
SELECTED = FLAT

# a base tab class
class Tab(Frame):
    def __init__(self, master, name):
        Frame.__init__(self, master)
        self.tab_name = name

# the bulk of the logic is in the actual tab bar
class TabBar(Frame):
    def __init__(self, master=None, init_name=None):
        Frame.__init__(self, master)
        self.tabs = {}
        self.buttons = {}
        self.current_tab = None
        self.init_name = init_name
        
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

if __name__ == '__main__':
    def write(x): print x
    
    thread.start_new_thread(weather.Update_Data, ())
    
    root.title("Thermostat")
        
    bar = TabBar(root, "Tempature Control")
        
    tab1 = Tab(root, "Tempature Control")				# notice how this one's master is the root instead of the bar
    #Label(tab1, text="Sunjay Varma is an extra ordinary little boy.\n\n\n\n\nCheck out his website:\nwww.sunjay-varma.com", bg="white", fg="red").pack(side=TOP, expand=YES, fill=BOTH)
    #Button(tab1, text="PRESS ME!", command=(lambda: write("YOU PRESSED ME!"))).pack(side=BOTTOM, fill=BOTH, expand=YES)
    #Button(tab1, text="KILL THIS TAB", command=(lambda: bar.delete("Wow..."))).pack(side=BOTTOM, fill=BOTH, expand=YES)

    #Button set up
    #display_CT.set(sTemp)
    frame_5 = Frame(tab1, height=3)
    frame_5.pack()
    button_Increase = tk.Button(frame_5, text = "++Increase", height = 3, width = 10)#, command = cmd_Inc)
    button_Decrease = tk.Button(frame_5, text = "--Decrease", height = 3, width = 10)#, command = cmd_Dec)
    button_Increase.pack(side=LEFT)
    button_Decrease.pack(side=RIGHT)
    
    #Heating, Cooling, Off radio button
    frame_4 = Frame(tab1)
    frame_4.pack()
    Radiobutton(frame_4, text="Heating", variable=Mode, value = 1).pack(side = LEFT)
    Radiobutton(frame_4, text="Off", variable=Mode, value = 0).pack(side = LEFT)
    Radiobutton(frame_4, text="Cooling", variable=Mode, value = 2).pack(side = LEFT)
        
    #Set Tempature Display
    frame_1 = Frame(tab1)
    frame_1.pack()
    label_1 = tk.Label(frame_1, text="Hold tempature:")
    label_1.pack(side = LEFT)
    label_SetTemp = tk.Label(frame_1, textvariable=display_HT, font=("Helvetica", 16), fg="orange")
    label_SetTemp.pack(side = RIGHT)
        
    #Current Tempature Display
    frame_2 = Frame(tab1)
    frame_2.pack()
    label_CT = tk.Label(frame_2, text="Current Temperature:")
    label_CT.pack(side=LEFT)
    Label_CT_Val = tk.Label(frame_2, textvariable=display_CT, font=("Helvetica", 16), fg="Green")
    Label_CT_Val.pack(side = RIGHT)
        
    #Current Humidity Display
    frame_3 = Frame(tab1)
    frame_3.pack()
    label_Hum = tk.Label(frame_3, text="Current Humidity:")
    label_Hum.pack(side=LEFT)
    Label_Hum_Val = tk.Label(frame_3, textvariable=display_Hum)
    Label_Hum_Val.pack(side = RIGHT)
    
    

    tab2 = Tab(root, "Outside Weather")
    #Label(tab2, text="How are you??", bg='black', fg='#3366ff').pack(side=TOP, fill=BOTH, expand=YES)
    #txt = Text(tab2, width=50, height=20)
    #txt.focus()
    #txt.pack(side=LEFT, fill=X, expand=YES)
    #Button(tab2, text="Get", command=(lambda: write(txt.get('1.0', END).strip()))).pack(side=BOTTOM, expand=YES, fill=BOTH)
    weather_OT.set(weather.get_Outside_Temp())
    #weather_OT = weather.get_Outside_Temp()
    frame_weather_1 = Frame(tab2)
    frame_weather_1.pack()
    Label(frame_weather_1, text="Outside Tempature:").pack()
    Label(frame_weather_1, textvariable=weather_OT , font=("Helvetica", 16), fg="Green").pack()
    weather.print_Info()
    
        
    tab3 = Tab(root, "Info")
    Label(tab3, bg='white', text="This tab was given as an argument to the TabBar constructor.\n\nINFO:\n").pack(side=LEFT, expand=YES, fill=BOTH)
        
    bar.add(tab1)                   # add the tabs to the tab bar
    bar.add(tab2)
    bar.add(tab3)
        
        #bar.config(bd=2, relief=RIDGE)			# add some border
        
    bar.show()
        
    root.mainloop()
