from datetime import datetime


def get_time(timestamp):
    date_object = datetime.fromtimestamp(timestamp)
    time = date_object.strftime("%A, %H : %M")
    return time



def get_Date(timestamp):
    date_object = datetime.fromtimestamp(timestamp)
    date = date_object.strftime("%A  %d/%m/%Y")
    return date
