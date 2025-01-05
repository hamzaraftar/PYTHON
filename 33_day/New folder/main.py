import requests


params =  {
    "lat":31.520370 ,
    "lng":74.358749,
}


response =  requests.get("https://api.sunrise-sunset.org/json" ,params=params)
response.raise_for_status()
data = response.json()
print(data)

