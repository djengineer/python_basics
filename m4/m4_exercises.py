########### Generate 5 random numbers into a list ###########

import random

my_list = [random.randint(-100,100),random.randint(-100,100),random.randint(-100,100),random.randint(-100,100),random.randint(-100,100)]
print(my_list)

###### add integer 3 to the back
my_list.append(3)
print(my_list)

####### insert between 4th and 5th element #######
my_list.insert(4,2.345)
print(my_list)

#### sort and update my_list #####

my_list = sorted(my_list)
print(my_list)
