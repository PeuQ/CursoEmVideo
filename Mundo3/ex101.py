#Create a method that determines if a person is in legal age to vote, and if its obligatory.
#method definition

def vote(birth_year):
  from datetime import date
  current_year = date.today().year
  if (current_year - birth_year < 16):
    return "DENIED"
  elif ((current_year-birth_year) >= 16) & ((current_year - birth_year) < 18):
    return "OPTIONAL"
  elif (current_year - birth_year >= 18):
    return "COMPULSORY"

#main
year = int(input("to determine if you are eligible to vote, enter the year you were born: "))

print(f'\n Your voting is {vote(year)}')
