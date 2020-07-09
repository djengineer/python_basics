####### Finding even or odd number #######

number = int(input("Type a Number: "))

if number%2 == 0:
    print("Number is an even number.")
    
elif number%2 ==1:
    print("Number is an odd number.")
    

    
    
####### Random number generator #######

from random import randint

# generates random integer
# generate a random integer between 0 and 3
number = randint(0,3)
print(number)



####### check if random number is even or odd #######

from random import randint
# generates random integer
# generate a random integer between 0 and 3
number = randint(0,3)
if number % 2 == 0:
    print("Number is an even number.")
    
elif number % 2 ==1:
    print("Number is an odd number.")
