from datetime import datetime

import time
import pytz


def get_time(timestamp):
    date_object = datetime.fromtimestamp(timestamp)
    time = date_object.strftime("%H : %M")
    return time


def get_Date(timestamp):
    date_object = datetime.fromtimestamp(timestamp)
    date = date_object.strftime("%A  %d/%m/%Y")
    return date


def get_Day(timestamp):
    date_object = datetime.fromtimestamp(timestamp)
    day = date_object.strftime("%A")
    return day

def _time ():
    t = time.localtime()
    current_time = time.strftime("%H:%M:%S", t)
    return current_time
print(_time())

def time2():
    tz_NY = pytz.timezone('Europe/Amsterdam')
    datetime_NY = datetime.now(tz_NY)
    print("NY time:", datetime_NY.strftime("%H:%M:%S"))