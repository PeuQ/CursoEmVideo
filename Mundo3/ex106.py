#function def: 
def my_help(command):
  title(f"Accessing help for {command}().")
  help(command)

def title(msg):
  my_len = len(msg)
  print('~' * my_len)
  print(msg)
  print('~' * my_len)
  
#main
command = ""
while True:
  title("Python Interactive Helping System")
  command = str(input("Enter Function or Library: "))
  if command.upper() == 'END':
    title("system operation terminated")
    break
  else:
    my_help(command)
