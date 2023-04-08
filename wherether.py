import requests

api_key = '73074604cc0ab0c5a2d01f9320daf782'
city = 'ho chi minh'
url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric'

response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    print(f'Temperature in {city}: {data["main"]["temp"]}°C')
else:
    print('Error occurred while fetching weather data')
