import datetime


def weekday_gen(d, end, excluded=(2, 3, 4, 5, 6, 7)):
    days = []
    while d.date() <= end.date():
        if d.isoweekday() not in excluded:
            days.append(d)
        d += datetime.timedelta(days=1)
    return days


print(weekday_gen(datetime.datetime(2019, 1, 1),
                  datetime.datetime(2019, 1, 30)))

