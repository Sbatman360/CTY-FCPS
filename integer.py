import datetime
import calendar
month = int(input("month: "))
year = int(input("year: ")
date = datetime.date(year, month, 13)
if(date.strftime("%a") == "Fri"):
  print("true")
else:
  print("false")

