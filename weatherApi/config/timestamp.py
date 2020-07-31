from datetime import datetime


def get_time(timestamp):
    date_object = datetime.fromtimestamp(timestamp)
    time = date_object.strftime("%A, %H : %M")
    return time


def get_Day(timestamp):
    date_object = datetime.fromtimestamp(timestamp)
    day = date_object.strftime("%A")
    return day
