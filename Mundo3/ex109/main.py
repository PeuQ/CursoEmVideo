import price

start_price = float(input("Enter the product's price: "))

print(f"An increase of 10% in {price.price_func(start_price)} results in {price.increase(start_price, 10, True)}\n")
print(f"A discount of 10% in {price.price_func(start_price)} results in {price.decrease(start_price, 10, True)}\n")
print(f"Doubling the starting price of {price.price_func(start_price)} results in {price.double(start_price, True)}\n")
print(f"Halving the starting price of {price.price_func(start_price)} results in {price.half(start_price, True)}\n")
