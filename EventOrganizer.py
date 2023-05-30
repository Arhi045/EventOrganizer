eventName = []
eventMonth = []
eventDay = []
eventYear = []

def validateDay(d, m, y):
  if m == 1:
    daysIn = 31
    if d <= daysIn and d > 0:
        return d
    else:
        d = int(input("Enter a valid day: "))
        while d > 31 or d < 1:
          d = int(input("Enter a valid day: "))
        return d
  elif m == 2:
    if y % 4 ==0 and y % 100 !=0 or y % 400 == 0:
      daysIn = 29
      if d <= daysIn and d > 0:
        return d
      else:
        d = int(input("Enter a valid day: "))
        while d > 29 or d < 1:
          d = int(input("Enter a valid day: "))
        return d
    else:
      daysIn = 28
      if d <= daysIn and d > 0:
        return d
      else:
        d = int(input("Enter a valid day: "))
        while d > daysIn or d < 1:
          d = int(input("Enter a valid day: "))
        return d
  elif m == 3:
    daysIn = 31
    if d <= daysIn and d > 0:
        return d
    else:
        d = int(input("Enter a valid day: "))
        while d > daysIn or d < 1:
          d = int(input("Enter a valid day: "))
        return d
  elif m == 4:
    daysIn = 30
    if d <= daysIn and d > 0:
        return d
    else:
        d = int(input("Enter a valid day: "))
        while d > daysIn or d < 1:
          d = int(input("Enter a valid day: "))
        return d
  elif m == 5:
    daysIn = 31
    if d <= daysIn and d > 0:
        return d
    else:
        d = int(input("Enter a valid day: "))
        while d > daysIn or d < 1:
          d = int(input("Enter a valid day: "))
        return d
  elif m == 6:
    daysIn = 30
    if d <= daysIn and d > 0:
        return d
    else:
        d = int(input("Enter a valid day: "))
        while d > daysIn or d < 1:
          d = int(input("Enter a valid day: "))
        return d
  elif m == 7:
    daysIn = 31
    if d <= daysIn and d > 0:
        return d
    else:
        d = int(input("Enter a valid day: "))
        while d > daysIn or d < 1:
          d = int(input("Enter a valid day: "))
        return d
  elif m == 8:
    daysIn = 31
    if d <= daysIn and d > 0:
        return d
    else:
        d = int(input("Enter a valid day: "))
        while d > daysIn or d < 1:
          d = int(input("Enter a valid day: "))
        return d
  elif m == 9:
    daysIn = 30
    if d <= daysIn and d > 0:
        return d
    else:
        d = int(input("Enter a valid day: "))
        while d > daysIn or d < 1:
          d = int(input("Enter a valid day: "))
        return d
  elif m == 10:
    daysIn = 31
    if d <= daysIn and d > 0:
        return d
    else:
        d = int(input("Enter a valid day: "))
        while d > daysIn or d < 1:
          d = int(input("Enter a valid day: "))
        return d
  elif m == 11:
    daysIn = 30
    if d <= daysIn and d > 0:
        return d
    else:
        d = int(input("Enter a valid day: "))
        while d > daysIn or d < 1:
          d = int(input("Enter a valid day: "))
        return d
  else:
    daysIn = 31
    if d <= daysIn and d > 0:
        return d
    else:
        d = int(input("Enter a valid day: "))
        while d > daysIn or d < 1:
          d = int(input("Enter a valid day: "))
        return d

def validateMonth(m):
  if m >= 1 and m <= 12:
    return m
  else:
    m = int(input("Enter a valid month (1-12): "))
    while m < 1 or m > 12:
      m = int(input("Enter a valid month (1-12): "))
    return m
    
def addEvent ():
  name = input("Enter event name: ")
  eventName.append(name)
  year = int(input("Enter event year: "))
  eventYear.append(year)
  month = int(input("Enter event month: "))
  month = validateMonth(month)
  eventMonth.append(month)
  day = int(input("Enter event day: "))
  day = validateDay(day, month, year)
  eventDay.append(day)

addEvent()
another = int(input("Do you want to enter another event? type (1) for yes and (2) for no: "))
i = 1
while (another == 1):
  i = i + 1
  addEvent()
  another = int(input("Do you want to enter another event? type (1) for yes and (2) for no: "))

for x in range(0, i):
  monthName = "none"
  if eventMonth[0] == 1:
    monthName = "January"
  elif eventMonth[0] == 2:
    monthName = "February"
  elif eventMonth[0] == 3:
    monthName = "March"
  elif eventMonth[0] == 4: 
    monthName = "April"
  elif eventMonth[0] == 5:
    monthName = "May"
  elif eventMonth[0] == 6:
    monthName = "June"
  elif eventMonth[0] == 7:
    monthName = "July"
  elif eventMonth[0] == 8:
    monthName = "August"
  elif eventMonth[0] == 9:
    monthName = "September"
  elif eventMonth[0] == 10:
    monthName = "October"
  elif eventMonth[0] == 11:
    monthName = "November"
  elif eventMonth[0] == 12:
    monthName = "December"
  elif eventMonth[0] == 13:
    monthName = "non existance"
  print("")
  print(eventName[x])
  print(monthName + " " + str(eventDay[x]) + ", " + str(eventYear[x]))
