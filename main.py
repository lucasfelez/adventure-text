import functions
from functions import generate_num
from functions import order_num

#generate a list of 5 random numbers
a = generate_num.generate(10)
completed = False

#order the list
print(a)

tries = 0
while not completed:
  a = generate_num.generate(1)
  print(a)
  tries += 1
  
  if a.__contains__(0):
    completed = True
    print("test succesful and took " + str(tries) + " tries")
  else:
    print("test failed")
