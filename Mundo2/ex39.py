#Military Enslitment
import datetime

birth_year = int(input("When were you born? "))
date = datetime.date.today()
year = date.strftime("%Y")
year_int = int(year)
age = year_int - birth_year

if(age == 18):
  print("Its time for your enlistment.")
elif(age > 18):
  print("Your time for enlistment has passed. By {} years exactly.".format(age - 18))
elif(age < 18):
  print("Your time for enlistment is still off by {} years.".format(18 - age))
