#functions for ex108

def increase(price=0, prct=0):
  final_price = (1+(prct/100)) * price

  return final_price

def decrease(price=0, prct=0):
  final_price = (1 - (prct/100)) * price

  return final_price

def double(price=0):
  final_price = price * 2

  return final_price

def half(price=0):
  final_price = price / 2

  return final_price

def price(price=0, coin="$"):
  return f"{coin}{price}"