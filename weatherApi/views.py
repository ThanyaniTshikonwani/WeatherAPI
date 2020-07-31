import requests
from django.shortcuts import render

from .config.remote import getUrl
from .config.timestamp import get_time, get_Day
from .forms import Post


def index(request):
    post = "Johannesburg"

    if request.method == "POST":
        form = Post(request.POST)

        if form.is_valid():
            post = form.cleaned_data.get('post')
    else:
        form = Post()
    get_weather = getUrl("weather", "metric") + post
    forecast_url = getUrl("forecast", "metric") + post

    response = requests.get(get_weather)
    forecast_response = requests.get(forecast_url)

    if forecast_response.status_code == 200:
        forecast_data = forecast_response.json()
        forecast_list = forecast_data["list"]
        selected_forecast = []

        for i in range(0, 7):
            timestamp = forecast_list[i]["dt"]
            time = get_time(timestamp)
            data_forecast_list = {
                "icon": forecast_list[i]["weather"][0]["icon"],
                "time": time,
                "temp": int(forecast_list[i]["main"]["temp"]),
                "weather": forecast_list[i]["weather"][0]["main"],
                "humidity": (forecast_list[i]["main"]["humidity"]),
                "temp_min": int(forecast_list[i]["main"]["temp_min"]),
                "temp_max": int(forecast_list[i]["main"]["temp_max"]),
            }

            selected_forecast.append(data_forecast_list)
    else:
        selected_forecast = {}

    if response.status_code == 200:

        data = response.json()
        timestamp = data["dt"]
        day = get_Day(timestamp)
        name = data["name"]
        day = day
        temp = data["main"]["temp"]
        country = data["sys"]["country"]
        description = data["weather"][0]["description"]
        temp_min = data["main"]["temp_min"]
        humidity = data["main"]["humidity"]
        temp_max = data["main"]["temp_max"]
        icon = data["weather"][0]["icon"]

        data_context = {
            "name": name,
            "day": day,
            "temp": int(temp),
            "country": country,
            "description": description,
            "temp_min": int(temp_min),
            "humidity": humidity,
            "temp_max": int(temp_max),
            "icon": icon,
            "Avg_Temp": int((temp_min + temp_max) / 2)
        }
    else:
        data_context = {}

    data_context["form"] = Post()
    data_context["selected_forecast"] = selected_forecast
    return render(request, 'views/index.html', data_context)
