import requests
api_key = "42205b7be76b414d497c3e44e81457a3"
OWM_ENDPOINT = "https://api.openweathermap.org/data/2.5/forecast"
weather_params = {
    "lat" : 31.561920,
    "lon" : 74.348083,
    "appid" : api_key,
}
response = requests.get(OWM_ENDPOINT, params=weather_params)
data = response.json()
print(data)