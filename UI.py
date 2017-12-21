import Tkinter as tk
from time import sleep
from Tkinter import *

top = tk.Tk()
display_CT = tk.IntVar()
display_CT = tk.IntVar()
display_Hum = tk.IntVar()
Mode = tk.IntVar()

setTemp = 60
curTemp = 60

class Page(tk.Frame):
    def __init__(self, *args, **kwargs):
        print ""
        tk.Frame.__init__(self, *args, **kwargs)
    pass
    def show(self):
        self.lift()
    pass

pass

class Page_Controls(Page):
    def __init__(self, *args, **kwargs):
        Page.__init__(self, *args, **kwargs)
        #Button set up
        display_CT.set(sTemp)
        frame_5 = Frame(top)
        frame_5.pack()
        button_Increase = tk.Button(frame_5, text = "++Increase", height = 3, width = 10, command = cmd_Inc)
        button_Decrease = tk.Button(frame_5, text = "--Decrease", height = 3, width = 10, command = cmd_Dec)
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
        label_1 = tk.Label(frame_1, text="Hold tempature:")
        label_1.pack(side = LEFT)
        label_SetTemp = tk.Label(frame_1, textvariable=display_CT, font=("Helvetica", 16), fg="orange")
        label_SetTemp.pack(side = RIGHT)

        #Current Tempature Display
        frame_2 = Frame(top)
        frame_2.pack()
        label_CT = tk.Label(frame_2, text="Current Temperature:")
        label_CT.pack(side=LEFT)
        Label_CT_Val = tk.Label(frame_2, textvariable=display_CT, font=("Helvetica", 16), fg="Green")
        Label_CT_Val.pack(side = RIGHT)

        #Current Humidity Display
        frame_3 = Frame(top)
        frame_3.pack()
        label_Hum = tk.Label(frame_3, text="Current Humidity:")
        label_Hum.pack(side=LEFT)
        Label_Hum_Val = tk.Label(frame_3, textvariable=display_Hum)
        Label_Hum_Val.pack(side = RIGHT)
pass

class Page_Forecast(Page):
    def __init__(self, *args, **kwargs):
           Page.__init__(self, *args, **kwargs)
           label = tk.Label(self, text="Forecast goes here")
           label.pack(side="top", fill="both", expand=True)
    pass
pass

class Page_Costs(Page):
    def __init__(self, *args, **kwargs):
           Page.__init__(self, *args, **kwargs)
           label = tk.Label(self, text="Cost goes here")
           label.pack(side="top", fill="both", expand=True)
    pass
pass

class Setup_UI(Page):
    def __init__(self, cmd_Inc, cmd_Dec, sTemp, cTemp):
        pControl = Page_Controls(self)
        pForecast = Page_Forecast(self)
        pCost = Page_Costs(self)

        buttonFrame = Frame(top)
        buttonFrame.pack(side=LEFT)

        containerFrame = Frame(top)
        containerFrame.pack()

        button_Controls = tk.Button(buttonFrame, text="Controls", height=3, width = 3, command=pControl.show)
        button_Forecast = tk.Button(buttonFrame, text="Forecast", height=3, width = 3, command=pForecast.show)
        button_Costs = tk.Button(buttonFrame, text="Costs", height=3, width = 3, command=pCost.show)
        button_Controls.pack()
        button_Forecast.pack()
        button_Costs.pack()

#       pControl.place(in_=containerFrame,x=0,y=0,relwidth=1,relheight=1)
#       pForecast.place(in_=containerFrame,x=0,y=0,relwidth=1,relheight=1)
#       pCost.place(in_=containerFrame,x=0,y=0,relwidth=1,relheight=1)
    pass
pass

def Default_setup1():
    print "Hit function 1"
pass

def Default_setup2():
    print "Hit function 2"
pass


if __name__ == "__main__":
    Setup_UI(Default_setup1, Default_setup2, setTemp, curTemp)
    top.mainloop()
