from datetime import datetime



def get_time(timestamp):
    date_object = datetime.fromtimestamp(timestamp)
    time = date_object.strftime("%H : %M %p")
    return time


def get_Date(timestamp):
    date_object = datetime.fromtimestamp(timestamp)
    date = date_object.strftime("%A  %d/%m/%Y")
    return date


def get_Day(timestamp):
    date_object = datetime.fromtimestamp(timestamp)
    day = date_object.strftime("%A")
    return day



