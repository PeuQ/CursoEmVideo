#loan calculations

house_price = float(input("How much is the house? "))
salary = float(input("How much is your salary? "))
pay_years = int(input("In how many years are going to pay? "))

#calculating monthly payments
monthly_pay = house_price / (pay_years * 12)

#calculating if loan is accepted
if(monthly_pay > salary * 0.3):
  print("\nUnfortunately, your loan can not be approved.")
else:
  print("\nYour loan has been approved!")
