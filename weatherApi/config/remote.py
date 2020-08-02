def getUrl(mode, units):
    baseUrl = "http://api.openweathermap.org/data/2.5/"
    baseUrl += mode + "?units=" + units + "&appid=7310a2a2bae0ac6e2153f2c53aa86e8b&q="

    return baseUrl


def getOneCallUrl(lat, lon):
    oneCallUrl = "https://api.openweathermap.org/data/2.5/onecall?"
    oneCallUrl += "lat=" + lat + "&lon=" + lon + "&exclude=current,minutely,hourly&units=metric&appid=7310a2a2bae0ac6e2153f2c53aa86e8b&q"
    return oneCallUrl

