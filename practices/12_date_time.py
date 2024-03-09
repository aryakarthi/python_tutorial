
# # data and time

import datetime as dt

# current date and time

current_date = dt.date.today()
print("Current Date : ", current_date)

current_time = dt.datetime.now()
print("Current Time : ", current_time)

# custom date and time

setdate = dt.date(2023, 9, 20)
print("Set Date : ", setdate)

print("Year : ", setdate.year)
print("Month : ", setdate.month)
print("Day : ", setdate.day)

settime = dt.time(10, 30, 15, 535353)
print("Set Time : ", settime)

print("Hours : ", settime.hour)
print("Minutes : ", settime.minute)
print("Seconds : ", settime.second)
print("Microseconds : ", settime.microsecond)

setdt = dt.datetime(2019, 3, 25, 10, 15, 30, 232435)
print("Set DateTime : ", setdt)
print("Set Date : ", setdt.date())
print("Set Time : ", setdt.time())

# difference between two datetimes

newyear25 = dt.datetime(2025, 1, 1)
diff = newyear25 - current_time
print("New Year 2025 in : ", diff)

# date and time format

print("Current Time : ", current_time)
s = current_time.strftime("%A %d %B %Y %I:%M %p")
print("Formatted Date : ", s)