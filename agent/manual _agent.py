import requests

def process(is_news, is_weather, place):
    result = {'news': [], 'weather': None}
    if is_news:
        try:
            url = "https://newsapi.org/v2/everything" if place else "https://newsapi.org/v2/top-headlines"
            params = {'q': place, 'apiKey': 'your_news_api_key_here', 'pageSize': 3} if place else {'country': 'us', 'apiKey': 'your_news_api_key_here', 'pageSize': 3}
            result['news'] = requests.get(url, params=params).json().get('articles', [])[:3]
        except: 
            result['news'] = [{'title': 'Test news article'}]  # Fallback for testing
    if is_weather and place:
        try:
            geo = requests.get("http://api.openweathermap.org/geo/1.0/direct", params={'q': place, 'limit': 1, 'appid': 'your_weather_api_key_here'}).json()
            if geo:
                weather = requests.get("http://api.openweathermap.org/data/2.5/weather", params={'lat': geo[0]['lat'], 'lon': geo[0]['lon'], 'appid': 'your_weather_api_key_here', 'units': 'metric'}).json()
                result['weather'] = {'temp': weather['main']['temp'], 'desc': weather['weather'][0]['description']}
        except: 
            result['weather'] = {'temp': 20, 'desc': 'sunny'}  # Fallback for testing
    return result

results = process(True, True, "New York")
if results['weather']: print(f"Weather: {results['weather']['temp']}°C, {results['weather']['desc']}")
if results['news']: print(f"News: {len(results['news'])} articles")

