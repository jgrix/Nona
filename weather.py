#import urllib.request
import urllib2
import json
import thread
import Tkinter as tk
from time import sleep

API_KEY = '00e4d3271410a849'


outside_temp = 0
relative_Humidity = 0
wind = "Null"
high = 0
low = 0



def Update_Data():
    global outside_temp, relative_Humidity, wind, high, low
    print("Making API  call")
    while True:
        f = urllib2.urlopen('http://api.wunderground.com/api/' + API_KEY + '/geolookup/conditions/q/MI/Livonia.json')
        json_string = f.read()
        print("parsing json")
        parsed_json = json.loads(json_string)
        outside_temp = parsed_json['current_observation']['temp_f']
        relative_Humidity = parsed_json['current_observation']['relative_humidity']
        wind = parsed_json['current_observation']['wind_string']
        #print(json_string)
        f.close()

        g = urllib2.urlopen('http://api.wunderground.com/api/' + API_KEY + '/forecast/q/MI/Livonia.json')
        
        json_string = g.read()
        parsed_json = json.loads(json_string)
        high = parsed_json['forecast']['simpleforecast']['forecastday'][0]['high']['fahrenheit']
        low = parsed_json['forecast']['simpleforecast']['forecastday'][0]['low']['fahrenheit']
        #print(json_string)
        g.close

        sleep(30)
pass

def get_High():
    return high
pass

def get_Low():
    return low
pass

def get_Outside_Temp():
    print outside_temp
    return outside_temp
pass

def get_Wind():
    return wind
pass

def get_Humidity():
    return relative_Humidity
pass

def print_Info():
    print("Updated Data")
    print("Outside Temp:", outside_temp)
    print("Relative Humidity:", relative_Humidity)
    print(wind)
    print("High: ", high)
    print("Low: ", low)
pass







if __name__ == "__main__":
    thread.start_new_thread(Update_Data, ())
    sleep(5)
    print("Updated Data")
    print("Outside Temp:", outside_temp)
    print("Relative Humidity:", relative_Humidity)
    print(wind)
    print("High: ", high)
    print("Low: ", low)
