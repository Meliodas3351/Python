import urllib.request
from urllib.parse import urlparse, urlencode
import json

s_city = "Lida,BY"
city_id = 0

appid = "d3222b950dc6fea8dbe97cce27217e81"

res = urllib.request.urlopen("http://api.openweathermap.org/data/2.5/find?q=Lida%2CBY&type=like&units=metric&APPID=d3222b950dc6fea8dbe97cce27217e81")
data = json.load(res)
print(data)
city_id = data['list'][0]['id']
print(str(city_id))

res = urllib.request.urlopen("http://api.openweathermap.org/data/2.5/forecast?id=626081&units=metric&lang=ru&APPID=d3222b950dc6fea8dbe97cce27217e81")
data = json.load(res)
print(data)
for i in data['list']:
    print(i['dt_txt'], '{0:+5.0f}'.format(i['main']['temp']), i['weather'][0]['description'])

