import datetime
from datetime import time





def log(setTemp, currentTemp, outsideTemp, high, low, furnance_firing):

    date_reg = datetime.date.today()
    time_reg = datetime.datetime.utcnow()
    tempStr = str(date_reg.year) + "-" + str(date_reg.month) + "-" + str(date_reg.day) + "-log.txt"
    try:
        myFile = open(tempStr, "a")
    except:
        print "Failed to open the file for output"
        return
    
    myFile.write("SetTemp:" + str(setTemp) + ", CurTemp:" + str(currentTemp) + ", outTemp:" + str(outsideTemp) + ", high:" + str(high) + ", low:" + str(low) + ", furn_fire:" + str(furnance_firing) + ", " + str(time_reg.hour) + ":" + str(time_reg.minute) + ":" + str(time_reg.second) + "\n")

    myFile.close()

pass


if __name__ == '__main__':

    #    openOutput()
    log("65","64","33","35","30","true")



