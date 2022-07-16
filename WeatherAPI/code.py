import requests as req
api_key = input('Enter your API key:')
city = input('City:')
r = req.get(f'http://api.weatherapi.com/v1/current.json?key={api_key}&q={city}&aqi=no')
#data = {'location': {'name': 'London', 'region': 'City of London, Greater London', 'country': 'United Kingdom', 'lat': 51.52, 'lon': -0.11, 'tz_id': 'Europe/London', 'localtime_epoch': 1657954739, 'localtime': '2022-07-16 7:58'}, 'current': {'last_updated_epoch': 1657953900, 'last_updated': '2022-07-16 07:45', 'temp_c': 16.0, 'temp_f': 60.8, 'is_day': 1, 'condition': {'text': 'Sunny', 'icon': '//cdn.weatherapi.com/weather/64x64/day/113.png', 'code': 1000}, 'wind_mph': 3.8, 'wind_kph': 6.1, 'wind_degree': 30, 'wind_dir': 'NNE', 'pressure_mb': 1025.0, 'pressure_in': 30.27, 'precip_mm': 0.0, 'precip_in': 0.0, 'humidity': 72, 'cloud': 0, 'feelslike_c': 16.0, 'feelslike_f': 60.8, 'vis_km': 10.0, 'vis_miles': 6.0, 'uv': 5.0, 'gust_mph': 5.4, 'gust_kph': 8.6}}
data = r.json()
temp = data['current']['temp_c']
name = data['location']['name']
last_updated = data['current']['last_updated']
text = data['current']['condition']['text']
humidity = data['current']['humidity']
feelslike_c = data['current']['feelslike_c']
print(
    f''' 
    Details are for {name} city\n
    The update time is: {last_updated}\n
    The current temperature is: {temp}\n
    It feels like {feelslike_c}\n
    Humidity is: {humidity}\n
    {text}\n    
    '''
)