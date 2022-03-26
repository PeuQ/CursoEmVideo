#dissecting a variable

var = input("Type something: ")

if(var.isalnum()):
  print("All characters are alphanumeric.")

if(var.isalpha()):
  print("All characters are alphabetic.")

if(var.isascii()):
  print("All characters are ASCII.")

if(var.isdecimal()):
  print("All characters are decimal.")

if(var.isdigit()):
  print("All Characters are digits.")

if(var.isidentifier()):
  print("Input contains only identifiers(underscores, digits and alphas).")

if(var.islower()):
  print("All characters are lower case.")

if(var.isupper()):
  print("All characters are upper case.")

if(var.isnumeric()):
  print("All characters are numeric.")

if(var.isprintable()):
  print("All characters are printable.")

if(var.isspace()):
  print("All characters are whitespaces.")

if(var.istitle()):
  print("the input is a title.")
