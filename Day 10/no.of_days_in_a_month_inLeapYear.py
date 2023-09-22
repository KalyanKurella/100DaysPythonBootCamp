"""def is_leap(year):
  if year % 4 == 0:
    if year % 100 == 0:
      if year % 400 == 0:
        print("Leap year.")
      else:
        print("Not leap year.")
    else:
      print("Leap year.")
  else:
    print("Not leap year.")"""

def days_in_month(leap_year, month):
  month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]  
  leap_month_days = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31] 
  if leap_year % 4 == 0:
    if leap_year % 100 == 0:
      if leap_year % 400 == 0:
        days = leap_month_days[month-1]
        return days
      else:
        days = month_days[month-1]
        return days
    else:
       days = leap_month_days[month-1]
       return days
  else:
    days = month_days[month-1]
    return days
#🚨 Do NOT change any of the code below 
year = int(input("Enter a year: "))
month = int(input("Enter a month: "))
days = days_in_month(year, month)
print(days)







