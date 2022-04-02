total = 0
over_1000 = 0
name_of_cheapest = ''
while True:
  name = str(input(("Name of the product: \n")))
  price = float(input("Price of the product: "))
  cheap = price
  name_of_cheapest = name
  total += price
  if(price > 1000):
    over_1000 += 1
  elif(price < cheap):
    cheap = price
    name_of_cheapest = name
  choice = str(input("\nWould you like to continue?[Y/N]: ")).strip().upper()
  if(choice == 'N'):
    break

print("Results:\nPurchase total: {}\nNumber of products over $1000: {}\nCheapest product: {}".format(total, over_1000, name_of_cheapest))
