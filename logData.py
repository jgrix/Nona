import datetime
from datetime import time





def logTemps(setTemp, currentTemp, outsideTemp, high, low, humidity, wind, furnance_firing):

    date_reg = datetime.date.today()
    time_reg = datetime.datetime.utcnow()
    tempStr = str(date_reg.year) + "-" + str(date_reg.month) + "-" + str(date_reg.day) + "-log.txt"
    try:
        myFile = open(tempStr, "a")
    except:
        print "Failed to open the file for output"
        return

    write1 = "SetTemp:" + str(setTemp) + ", CurTemp:" + str(currentTemp) + ", outTemp:" + str(outsideTemp)
    write2 = ", high:" + str(high) + ", low:" + str(low) + ", Humidity:" + str(humidity) + ", Wind:" + str(wind)
    write3 = ", furn_fire:" + str(furnance_firing) + ", " + str(time_reg.hour) + ":" + str(time_reg.minute) + ":" + str(time_reg.second) + "\n"
    
    myFile.write(write1 + write2 + write3 )

    myFile.close()

pass

def logFurnance(firing):
    fileName = "Furnance_Firing_Log.txt"
    date = datetime.date.today()
    time = datetime.datetime.utcnow()
    status = "Unknown"
    
    if firing:
        status = "On"
    else:
        status = "Off"

    try:
        myFile = open(fileName, "a")
    except:
        print "Failed to open the file"
        return

    myFile.write(str(date) + " " + str(time) + " " + status + "\n")



pass


if __name__ == '__main__':

    #    openOutput()
    logTemps("65","64","33","35","30","true")
    logFurnance(True)



