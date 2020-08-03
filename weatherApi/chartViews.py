import requests
from django.http import JsonResponse

from django.shortcuts import render

from .config.remote import getUrl, getOneCallUrl
from .config.timestamp import get_Day
from .forms import Post


def chart(request):
    def post():
        post = "Johannesburg"

        if request.method == "POST":
            form = Post(request.POST)

            if form.is_valid():
                post = form.cleaned_data.get('post')

        get_weather = getUrl("weather", "metric") + post
        return get_weather

    response = requests.get(post())

    def get_weatherCoords():
        try:
            getCoord = response.json()
            lon = getCoord["coord"]["lon"]
            lat = getCoord["coord"]["lat"]
        except Exception as  e:
            return render(request, 'views/index.html')

        get_daily_weather = getOneCallUrl(str(lat), str(lon))
        get_daily_weather_response = requests.get(get_daily_weather)

        return get_daily_weather_response

    if get_weatherCoords().status_code == 200:
        try:
            get_daily_weather_response_data = get_weatherCoords().json()
        except Exception as e:
            return render(request, 'views/index.html')
        get_daily_weather_response_list = get_daily_weather_response_data["daily"]

        data_temp_min = []
        data_temp_max = []
        data_days = []
        data_temp_avg = []

        for i in range(0, 7):
            timestamp = get_daily_weather_response_list[i]["dt"]

            day = get_Day(timestamp)
            day_temp_min = int(get_daily_weather_response_list[i]["temp"]["min"])
            day_temp_max = int(get_daily_weather_response_list[i]["temp"]["max"])
            day_temp_avg = int((day_temp_min + day_temp_max) / 2)


            data_temp_min.append((day_temp_min))
            data_temp_max.append(day_temp_max)
            data_days.append(day)
            data_temp_avg.append(day_temp_avg)

        daily_data = {
            "LowTemp": data_temp_min,
            "HighTemp": data_temp_max,
            "AvgTemp": data_temp_avg,
            "Days": data_days,
        }
        print(daily_data)
        return JsonResponse(daily_data)
    else:
        daily_forecast = {}

    return render(request, 'views/index.html', )
