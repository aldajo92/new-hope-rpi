import datetime
import time


def get_time_name():
    ts = time.time()
    st = datetime.datetime.fromtimestamp(ts).strftime('%Y%m%d%H%M%S')
    return st


def image_time_name():
    name = get_time_name()
    name += '.jpg'
    return name

print image_time_name()
