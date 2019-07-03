import datetime 
import random

def random_datetime(start_datetime, end_datetime):
    delta = end_datetime - start_datetime
    inc = random.randrange(delta.total_seconds())
    return start_datetime + datetime.timedelta(seconds=inc)

if __name__=='__main__':
    start_datetime = datetime.datetime(2018, 6, 17, 10, 0, 0)
    end_datetime = datetime.datetime(2018, 12, 17, 18, 0, 0)
    for i in range(1, 20): 
        dt = random_datetime(start_datetime, end_datetime)
        print("{\"time\": \"%s\"}," % dt)
