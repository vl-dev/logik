import random
from check import check

numbers = 8
selLength = 5

selection = [random.randint(1, numbers) for x in range(selLength)]

won = False
for i in range(10):
  putinString = input()
  putin = list(map(int, putinString.split(",")))
  print(check(selection,putin))
  
  if putin == selection:
    won = True
    break

if won:
  print("Vyhlaaal")

else:
  print("Plohlaal")

print(selection)