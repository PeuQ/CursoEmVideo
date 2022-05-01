#create a program with a metho named 'counter()',. which receives 3 parameters, start, end and step. your program must make 3 types of counting. from 1 to 10, 1 by 1, from 10 to 0, 2 by 2, and a customized counting.
from time import sleep

def counter(start, end, step):
  print(f"\ncounting from {start} to {end}, {step} by {step}")
  sleep(2.0)

  if(step < 0):
    step += -1
  elif(step == 0):
    step = 1

  if(start < end):
    c = start
    while c <= end:
      print(f"{c}", end=' ', flush=True)
      sleep(0.5)
      c += step
  else:
    c = start
    while c >= end:
      print(f"{c}", end=' ', flush=True)
      sleep(0.5)
      c -= step
#main
#a) 1 to 10, 1 by 1.
counter(1, 10, 1)
#b) 10 to 0, 2 by 2
counter(10, 0, 2)
#c) custom
print("\nYour custom counting!")
start = int(input("start: "))
end = int(input("end: "))
step = int(input("step: "))
counter(start, end, step)
