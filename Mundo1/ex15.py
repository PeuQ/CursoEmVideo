#calculate how much to pay for a rented car.

#$60/day && $0.15/Km

days = int(input("How many days did you rent teh car for? "))

km = float(input("\nHow many Km's were traversed during your rent? "))

price_for_days = days * 60
price_for_km = km * 0.15

full_price = price_for_days + price_for_km

print("Your rental comes at ${:.2f}".format(full_price))
