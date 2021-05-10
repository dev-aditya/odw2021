from datetime import datetime

# Quick and rough gps calculator (fra)
# Don't change this; it is the beginning of the gps time count
gps_begin = datetime(1980, 1, 6, 0, 0, 0)

year = int(input('Year: '))
month = int(input('Month: '))
day = int(input('Day: '))
hour = int(input('Hour: '))
minute = int(input('Minute: '))
second = int(input('Second: '))
# The day and time we want to analyse
# 10th of August 2017, 00:26:22
the_day = datetime(year, month, day, hour, minute, second)

leap_seconds = 18  # as of Dec 2016
gps = int((the_day - gps_begin).total_seconds()) + leap_seconds
print('GPS time: ' + str(gps))
