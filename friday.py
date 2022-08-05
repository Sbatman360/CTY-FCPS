import datetime
import calendar
def friday(month, year):
  month = int(input("month: "))
  list = []
  for i in range(year, year + 10): 
    date = datetime.date(i, month, 13)
  if(date.strftime("%a") == "Fri"):
    list.append(i)
  else:
    pass
  