#get the birth year of 7 people and show which are underage and which are not.
#consider underage == under 18
from datetime import date
todays_date = date.today()
this_year = todays_date.year

#counting
underage_count = 0
not_underage_count = 0
for i in range(0, 7):
  year = int(input("When were you born?(year): "))
  if((this_year - year) < 18):
    underage_count += 1
  else:
    not_underage_count += 1

#printing final result
print("There are {} people who are underage\nAnd, {} people who are not underage.".format(underage_count, not_underage_count))
