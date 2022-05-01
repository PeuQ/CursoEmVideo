#create a module name "price.py" with the functions increase(), decrease(), double() and half(). Also make a program that imports and uses this module's functions.

import price

start_price = float(input("Enter the product's price: "))

print(f"An increase of 10% in ${start_price} results in ${price.increase(start_price, 10)}\n")
print(f"A discount of 10% in ${start_price} results in ${price.decrease(start_price, 10)}\n")
print(f"Doubling the starting price of ${start_price} results in ${price.double(start_price)}\n")
print(f"Halving the starting price of ${start_price} results in ${price.half(start_price)}\n")
