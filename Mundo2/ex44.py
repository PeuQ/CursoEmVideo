#calculate the value to be paid by the original price of the product and method of payment.
price = float(input("Enter the price of the product: "))

choice = int(input("How would you like to pay:\n1 - full on money/check(10% discount)\n2 - full on card(5% discount)\n3 - 2x on card(no discount)\n4 - 3x or more on card(20% interest)\n"))

if(choice == 1):
  print("Your total comes to ${}".format(price * 0.9))
elif(choice == 2):
  print("Your total comes to ${}".format(price * 0.95))
elif(choice == 3):
  print("Your total comes to ${}".format(price))
elif(choice == 4):
  portions = int(input("How many portions will you divide your payment?: "))
  print("Your payment will be divided in {} portions of ${} with a 20% interest in total".format(portions, price/portions))
  print("Your total comes to ${}".format(price * 1.2))
