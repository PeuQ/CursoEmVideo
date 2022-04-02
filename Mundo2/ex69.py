#group data
#parameters
over_18 = 0
number_of_males = 0
women_under_20 = 0
while True:
  sex = str(input("Male or Female?[M/F]: ")).strip().upper()
  age = int(input("How old are you?: "))

  if(age >= 18):
    over_18 += 1
  elif(sex == 'M'):
    number_of_males += 1
  elif(sex == 'F') and (age < 20):
    women_under_20 += 1
  
  choice = str(input("\nWould you like to continue?[Y/N]: ")).strip().upper()
  if(choice == 'N'):
    break
print("Registered:\n{} People over 18 years old\n{} males\n{} women under 20 years old".format(over_18, number_of_males,women_under_20))
