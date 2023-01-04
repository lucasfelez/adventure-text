import random
import time



def generate(how_many):
  estimated_time = round(0.0255665555 * how_many,2)
  
  nums = []
  print("the estimared time is: " + str(estimated_time) + "seconds")
  
  start_time = time.time()
  for i in range(how_many):
    nums.append(random.randint(0,how_many*5))
    print("left to generate is:",how_many-len(nums))
    time.sleep(0.02555)
    
  print("it took " + str(round(time.time()-start_time, 2)) + " seconds to generate " + str(how_many) + " numbers")
  return nums

