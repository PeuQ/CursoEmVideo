#functions for "pricing.py"

def increase(price=0, prct=0, format_o=False):
  '''
-> Calculates the increase in the price of a product.
:param price: the original price.
:param pcrt: percentage of increase.
:param format_o: formats the output.
:return: the return value of the function.
'''
  result = (1+(prct/100)) * price

  return result if format_o is False else price_func(result)

def decrease(price=0, prct=0, format_o=False):
  '''
-> Calculates the discount in the price of a product.
:param price: the original price.
:param pcrt: percentage of discount.
:param format_o: formats the output.
:return: the return value of the function.
'''
  result = (1 - (prct/100)) * price
  
  return result if format_o is False else price_func(result)

def double(price=0, format_o=False):
  result = price * 2
  
  return result if format_o is False else price_func(result)
  
def half(price=0, format_o=False):
  result = price / 2
  
  return result if format_o is False else price_func(result)

def price_func(price=0, coin="$"):
  return f"{coin}{price:>.2f}"

def summary(price=0, inc_prct=10, dis_prct=10):
  print('-'*30)
  print("Pricing Summary:".center(30))
  print('-'*30)

  print(f"Original Price: {price_func(price)}.")
  print(f"Double Price: {double(price, True)}")
  print(f"Double Price: {half(price, True)}")
  print(f"{inc_prct}% Increase: {increase(price, inc_prct, True)}.")
  print(f"{dis_prct}% Decrease: {decrease(price, dis_prct, True)}.")
  print('-'*30)
