from datetime import date

import datetime
from datetime import date
from datetime import timedelta

# ------------------------------------- part 1

date_entry1 = input('Enter a date1 in YYYY-MM-DD format :')
year1, month1, day1 = map(int, date_entry1.split('-'))
date1 = datetime.date(year1, month1, day1)
date_entry2 = input('Enter a date2 in YYYY-MM-DD format :')
year2, month2, day2 = map(int, date_entry2.split('-'))
date2 = datetime.date(year2, month2, day2)
print('date1 :', date1)
print('date2 :', date2)

d = date2 - date1
print('result seconds :', d.days * 86400)


# ------------------------------------- part 2

def calNum(year):
    return (year // 4) - (year // 100) + (year // 400)


def leapNum(l, r):
    l -= 1
    num1 = calNum(r)
    num2 = calNum(l)
    print(num1 - num2)


if __name__ == "__main__":
    l1 = year1
    r1 = year2
    leapNum(l1, r1)



# ------------------------------------- part 3

def gregorian_to_jalali(gy, gm, gd):
    g_d_m = [0, 31, 59, 90, 120, 151, 181, 212, 243, 273, 304, 334]
    if gm > 2:
        gy2 = gy + 1
    else:
        gy2 = gy
    days = 355666 + (365 * gy) + ((gy2 + 3) // 4) - ((gy2 + 99) // 100) + ((gy2 + 399) // 400) + gd + g_d_m[gm - 1]
    jy = -1595 + (33 * (days // 12053))
    days %= 12053
    jy += 4 * (days // 1461)
    days %= 1461
    if days > 365:
        jy += (days - 1) // 365
        days = (days - 1) % 365
    if days < 186:
        jm = 1 + (days // 31)
        jd = 1 + (days % 31)
    else:
        jm = 7 + ((days - 186) // 30)
        jd = 1 + ((days - 186) % 30)
    return [jy, jm, jd]


print('date1 :', gregorian_to_jalali(year1, month1, day1))
print('date2 :', gregorian_to_jalali(year2, month2, day2))
