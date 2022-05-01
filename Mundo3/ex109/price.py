#functions for ex109

def increase(price=0, prct=0, format_o=False):
  result = (1+(prct/100)) * price

  return result if format_o is False else price_func(result)

def decrease(price=0, prct=0, format_o=False):
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
