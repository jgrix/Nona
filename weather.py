import urllib.request
import json
import _thread
from time import sleep

API_KEY = '00e4d3271410a849'

outside_temp = 0
relative_Humidity = 0
wind_String = "Null"
high = 0
low = 0



def Update_Data():
    global outside_temp, relative_Humidity, wind_String, high, low
    print("Making API  call")
    while True:
        f = urllib.request.urlopen('http://api.wunderground.com/api/' + API_KEY + '/geolookup/conditions/q/MI/Livonia.json')
        json_string = f.read()
        print("parsing json")
        parsed_json = json.loads(json_string)
        outside_temp = parsed_json['current_observation']['temp_f']
        relative_Humidity = parsed_json['current_observation']['relative_humidity']
        wind_String = parsed_json['current_observation']['wind_string']
        print(json_string)
        f.close()

        g = urllib.request.urlopen('http://api.wunderground.com/api/' + API_KEY + '/forecast/q/MI/Livonia.json')
        json_string = g.read()
        parsed_json = json.loads(json_string)
        high = parsed_json['forecast']['simpleforecast']['forecastday'][0]['high']['fahrenheit']
        low = parsed_json['forecast']['simpleforecast']['forecastday'][0]['low']['fahrenheit']
        print(json_string)
        g.close()
        sleep(3600)
pass

def get_High():
    return high
pass

def get_Low():
    return low
pass

def get_Outside_Temp():
    return outside_temp
pass

def get_Wind():
    return wind_String
pass








if __name__ == "__main__":
    _thread.start_new_thread(Update_Data, ())
    sleep(5)
    print("Updated Data")
    print("Outside Temp:", outside_temp)
    print("Relative Humidity:", relative_Humidity)
    print(wind_String)
    print("High: ", high)
    print("Low: ", low)
