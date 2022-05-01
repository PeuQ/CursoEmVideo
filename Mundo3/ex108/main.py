#To ex107 add the function price() that shows the value as a formatted price value.

import price

start_price = float(input("Enter the product's price: "))

print(f"An increase of 10% in {price.price(start_price)} results in {price.price(price.increase(start_price, 10))}\n")
print(f"A discount of 10% in {price.price(start_price)} results in {price.price(price.decrease(start_price, 10))}\n")
print(f"Doubling the starting price of {price.price(start_price)} results in {price.price(price.double(start_price))}\n")
print(f"Halving the starting price of {price.price(start_price)} results in {price.price(price.half(start_price))}\n")
