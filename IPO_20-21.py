import requests

s_city = "Lida,BY"
city_id = 1

appid = "d3222b950dc6fea8dbe97cce27217e81"
try:
    res = requests.get("http://api.openweathermap.org/data/2.5/find",
                 params={'q': s_city, 'type': 'like', 'units': 'metric', 'APPID': appid})
    data = res.json()
    print(res.url)

    # получаем пакет в формате JSON.
    # Разбираем пакет и получаем нужные значения по названиям полей
    cities = ["{} ({})".format(d['name'], d['sys']['country'])
              for d in data['list']]
    print("city:", cities)
    city_id = data['list'][0]['id']
    print('city_id=', city_id)
except Exception as e:
    print("Exception (find):", e)
    pass
try:
    res = requests.get("http://api.openweathermap.org/data/2.5/forecast",
                       params={'id': city_id, 'units': 'metric', 'lang': 'ru', 'APPID': appid})
    data = res.json()
    print(data)
    for i in data['list']:
        print(i['dt_txt'], '{0:+5.0f}'.format(i['main']['temp']), i['weather'][0]['description'])
        #Часть до точки определяет минимальную ширину,Часть после точки урезает десятичную часть
    print(res.url)
except Exception as e:
    #print("Exception (forecast):", e)
    pass