from datetime import datetime
import datetime
import json
import requests
"""
program gets information about weather in Moscow
via API https://openweathermap.org/api:
- день с миним. разницей "ощущаемой" и фактической температуры ночью
- макс. продолжительность светового дня с указанием даты
за 5 дней вперед считая текущую дату

"""

def day_transformate(day):
    val = datetime.datetime.fromtimestamp(int(day))
    return f"{val:%Y-%m-%d}"

def time_transform(tm): 
    val = datetime.datetime.fromtimestamp(int(tm))
    return val

def light_day(d1,d2):  
    day_length = abs(d2 - d1)
    return day_length

api_key = '**************************'
lon = '37.606667'
lat = '55.761665'

time_data = {} 
temp_amplitude = {} 

try:
    request = requests.get(f'https://api.openweathermap.org/data/2.5/onecall?lat={lat}&lon={lon}&appid={api_key}&units=metric') 
    weather_data = json.loads(request.text)

except Exception as e:
    print('Something is wrong while connection! Error:', e)


try:
    for i in range(len(weather_data['daily'])-3): 
        
        temp_amplitude[day_transformate(weather_data['daily'][i]['dt'])] =\
             abs(weather_data['daily'][i]['temp']['night'] - weather_data['daily'][i]['feels_like']['night'])
        
        time_data[day_transformate(weather_data['daily'][i]['dt'])] =\
            light_day((time_transform(weather_data['daily'][i]['sunset'])),
            (time_transform(weather_data['daily'][i]['sunrise'])))

except Exception as e:
    print('Something is wrong! Cannot extract data:', e)


max_light_day = max(time_data.values())
final_day = {k:v for k, v in time_data.items() if v==max_light_day}

for k, v in final_day.items():
    print('Максимальная продолжительность светового дня:', str(v), 'день:', k)

min_amplitude = min(temp_amplitude.values())
final_amplitude = {k:v for k, v in temp_amplitude.items() if v==min_amplitude}

for k, v in final_amplitude.items():
    print('Минимальная разница "ощущаемой" и фактической температуры ночью:', v, 'день:', k)

