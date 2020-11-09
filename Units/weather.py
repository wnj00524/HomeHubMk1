from pyowm import OWM
import Units.tools as tools
import time as t
import os
import numpy as np


class weather():
    temp = ""
    wind_speed = ""
    desc = ""
    got_time = ""

wt = weather()

def first_run_check():
    file = 'weather.npy'
    dirs = os.getcwd().split("\\")[-1].lower()
    if dirs == "homehubmk1":
        file = os.getcwd() + "\\Units\\" + file
    if os.path.isfile(file) == False:
        return True
    else:
        return False

def saved_weather_file_path(file):
    dirs = os.getcwd().split("\\")[-1].lower()
    if dirs == "homehubmk1":
        file = os.getcwd() + "\\Units\\" + file
    return file

def save_weather(w, rec_time):
    fileN = "weather.npy"
    tools.save_setting("time_got",rec_time,fileN)
    tools.save_setting("temp", w.temperature('celcius')['temp'], fileN)
    tools.save_setting()
    #todo 1:Work out what data to be saved.



def get_weather(location, say_it):
    key = tools.get_setting("owm","settings.npy")
    owm = OWM(key)
    mgr = owm.weather_manager()
    if first_run_check():
        obs = mgr.weather_at_place(location)
        w = obs.weather
        save_weather(w, obs.rec_time)
    else:
        #todo 2: Check when the weather last updated and if more than ten minutes update the weather.
        w = np.load(saved_weather_file_path("weather.npy"),allow_pickle=True)






#w.detailed_status         # 'clouds'
#w.wind()                  # {'speed': 4.6, 'deg': 330}
#w.humidity                # 87
#print(w.temperature('celsius'))  # {'temp_max': 10.5, 'temp': 9.7, 'temp_min': 9.0}
#w.rain                    # {}
#w.heat_index              # None
#w.clouds                  # 75



