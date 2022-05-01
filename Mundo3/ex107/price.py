#functions for ex107

def increase(price, prct):
  final_price = (1+(prct/100)) * price

  return final_price

def decrease(price, prct):
  final_price = (1 - (prct/100)) * price

  return final_price

def double(price):
  final_price = price * 2

  return final_price

def half(price):
  final_price = price / 2

  return final_price
