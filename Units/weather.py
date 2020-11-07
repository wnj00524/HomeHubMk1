from pyowm import OWM
#fbe4f9d1065cee2333cf810e8bdf37ea


owm = OWM('fbe4f9d1065cee2333cf810e8bdf37ea')
mgr = owm.weather_manager()
obs = mgr.weather_at_place('Sevenoaks, GB')
w = obs.weather

w.detailed_status         # 'clouds'
w.wind()                  # {'speed': 4.6, 'deg': 330}
w.humidity                # 87
print(w.temperature('celsius'))  # {'temp_max': 10.5, 'temp': 9.7, 'temp_min': 9.0}
w.rain                    # {}
w.heat_index              # None
w.clouds                  # 75
print(w.detailed_status)