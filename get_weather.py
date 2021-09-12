import re
import requests


def get_weather(lat: str, lon: str):
    api_url = "https://api.weather.yandex.ru/v1/forecast?lat=%s&lon=%s" % (lat, lon)
    api_key = {'X-Yandex-API-Key': '5a05a374-f3bd-4bd2-b4a5-f02502ff8af8'}
    response = requests.get(api_url, headers=api_key)
    data = response.json()
    fact = data['fact']
    conditions_ru = {
        'clear': 'ясно',
        'partly-cloudy': 'малооблачно',
        'cloudy': 'облачно с прояснениями',
        'overcast': 'пасмурно',
        'partly-cloudy-and-light-rain': 'небольшой дождь',
        'partly-cloudy-and-rain': 'дождь',
        'overcast-and-rain': 'сильный дождь',
        'overcast-thunderstorms-with-rain': 'сильный дождь, гроза',
        'cloudy-and-light-rain': 'небольшой дождь',
        'overcast-and-light-rain': 'небольшой дождь',
        'cloudy-and-rain': 'дождь',
        'overcast-and-wet-snow': 'дождь со снегом',
        'partly-cloudy-and-light-snow': 'небольшой снег',
        'partly-cloudy-and-snow': 'снег',
        'overcast-and-snow': 'снегопад',
        'cloudy-and-light-snow': 'небольшой снег',
        'overcast-and-light-snow': 'небольшой снег',
        'cloudy-and-snow': 'снег'
    }
    wind_dir_ru = {
        'nw': 'северо-западное',
        'n': 'северное',
        'ne': 'северо-восточное',
        'e': 'восточное',
        'se': 'юго-восточное',
        's': 'южное',
        'sw': 'юго-западное',
        'w': 'западное',
        'с': 'штиль'
    }
    print()
    print('Температура =', fact['temp'], 'градусов по Цельсию')
    print('Ощущается как =', fact['feels_like'], 'градусов по Цельсию')
    print('Описание :', conditions_ru[fact['condition']])
    print('Скорость ветра =', fact['wind_speed'], 'м/с')
    print('Направление ветра :', wind_dir_ru[fact['wind_dir']])
    print('Атмосферное давление =', fact['pressure_mm'], 'мм рт. ст.')
    print('Влажность воздуха =', str(fact['humidity']) + '%')

    
if __name__ == "__main__":
    lat = input('Введите широту : ')
    lon = input('Введите долготу : ')
    get_weather(lat, lon)
