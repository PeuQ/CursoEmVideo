#give the salaries a raise.
#if salary > 1250.00 => *1.1
#if salary < 1250.00 => *1.15

salary = float(input("Enter your current salary: "))

if(salary > 1250.00):
  print("You have receveid a 10% raise! Your new salary is ${:.2f}".format(salary * 1.1))
elif(salary <= 1250.00):
  print("You have receveid a 15% raise! Your new salary is ${:.2f}".format(salary * 1.15))
