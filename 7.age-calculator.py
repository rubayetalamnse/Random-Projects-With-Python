import datetime
from datetime import date

date_of_birth = date(2000, 11, 4)
today_date = date.today()

age = today_date.year-date_of_birth.year - \
    ((today_date.month, today_date.day) < (date_of_birth.month, date_of_birth.day))

print("Your age is" ,age)
