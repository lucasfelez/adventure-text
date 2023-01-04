import functions
from functions import generate_num
from functions import order_num

#generate a list of 5 random numbers
numsf = generate_num.generate(5)
print(numsf)

#order the list in ascending order
numsford = order_num.order_num(numsf,False)
print(numsford)

