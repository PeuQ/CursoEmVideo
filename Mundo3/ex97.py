#special kind of print

def write(msg):
  length = len(msg) + 5

  print("~"*length)
  print(f"  {msg}")
  print("~"*length)

#main
title = str(input("Write your title: "))
print("\n\n")
write(title)
