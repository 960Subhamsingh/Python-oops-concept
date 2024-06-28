# import datetime library
import datetime
import calendar 

# see today date
today = datetime.date.today()
print(today)

# see , which  week day is going on this month
# weekday() - Monday is 0 and Sunday is 6
today.isoweekday()

# see , which week day is going on this month
# isoweekday() - Monday is 1 and Sunday is 7
today.weekday()

# see the calendar of 2024
print(calendar.calendar(2024))

# see the month , with use month format
print(calendar.month(2024,6,25))

# see the date, month , year using date function
d = datetime.date(2024, 9 ,12)
print(d)

# see how many weekdays of this month
print(calendar.weekday(2024,2,2))

# see, this year is a leap year 2024
print(calendar.isleap(2024))

# see the leapday of this to year below
print(calendar.leapdays(2002, 2024))

# see the datemonth to using Strptime format
dt_str = 'July 24, 2024'
datetime.datetime.strptime(dt_str,'%B %d, %Y')

 







