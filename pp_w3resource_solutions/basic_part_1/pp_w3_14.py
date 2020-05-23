from datetime import date
date1 = date(2020,5,21)
date2 = date(1996,11,8)

delta = date1 - date2
print(delta.days)