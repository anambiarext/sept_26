import datetime

def friday_the_13th(month, year):
    date = datetime.date(year, month, 13)
    day = date.weekday()
    return day == 4

print(friday_the_13th(4, 2023))
