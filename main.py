import functions
from functions import generate_num
from functions import order_num

numsf = generate_num.generate(5)
print(numsf)
numsford = order_num.order_num(numsf,False)
print(numsford)