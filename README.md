# Python Basics
Created by Wong Ding Jie
Copyright 2018 - 2020

# Introduction/Requirements

Python 3.6

Python 3.6 is compatible with PyGame.

Other resources:
IDLE - Default Python Integrated Environment (IDE))
Using PIP package manager for Python

If you install Python onto your own computer:
- https://www.python.org/downloads/release/python-369/
- https://www.python.org/downloads/

Once you installed Python3.6, you can use IDLE to run your codes.
To install PyGame, in the search bar on Windows, run cmd.exe
Run the following command in the command line:

`pip install pygame` or `pip3 install pygame`

# Module 1 : Installation , user inputs and comments

## Getting user inpput

Getting the raw input from the command line:
`input(“What is your name”)`

Line break in the command:

`input(“What is your name\n>>>>”)`

A form input for would look something like this:

```
print(
    "your name is",
    input("what is your name?\n>>>"),
    "\nyour age is",
    input("what is your age?\n>>>"),
    "\nyour hobby",
    input("what is your hobby?\n>>>")
)
```
## Commenting

Commenting is important for people to read and understand your code. Often, we will forget what or why we wrote a piece of code.

Commenting:
"#" using hashtag / hex symbol will set comments for your code
"#" can only comment one line at a time, no multipleline commenting in python

## Exercises and Activities :
Create a form to ask questions to your classmates, or anyone near you.
- For example your dreams, favourite food, favourite colour, etc
- Have them fill up the answers
- Create a form to ask your friend / parents some questions
- Show the program to them and let them answer

======================================================
# Module 2 : Data Manipulation Variables, Datatypes and Math 

## Variables

Variables are like your variables in algebra. It can be a number, text or logic like True or False. 

Declaring a variable:

```
name  = “John”
print(name)
```

Printing out a variable:

```
name = input("What is your name?")
age = input("What is your age?")
print("My name is",name,"\nI am",age,"years old.")
```

## Datatypes

1. String data type: "It is declared with a doublequote"
2. Integer data type:  Whole Numbers
3. Float data type: numbers with decimal places
4. Boolean data type: True or False

### Converting Data Types: 

```
# from string to integer
mystring = "10" # this is an integer
converted_number = str(number)
print(type(converted_number)

# from integer to string
number = 10 # this is an integer
converted_number = str(number)
print(type(converted_number)

```

### Declaring Boolean Variable:

```
# using boolean data types
my_var = True
my_var_2 = bool(0) # what is the value of my_var_2?
my_var_3 = bool(1) # what is the value of my_var_3?
# try using other numbers
```

## Math

### Basic Math operators

| Sign          | Meaning       |
| ------------- |:-------------:|
| +             | add           |
| -             | minux         |
| *             | multiply      |
| /             | divide        |
| **            | exponential   |
| %             | modulo, to find the remainder of the division      |


### To import the math library: 
To use math functions, we need to import a pre-included library from Python

`import math # at the start of the py file`

To use Pi for example:

`from math import pi # at the start of the py file`

To use trigonometry:

```
math.cos(variable)
math.tan(variable)
math.sin(variable)
```
Math reference: https://docs.python.org/3/library/math.html

#### Examples:

```
import math
from math import pi

# Area of circle of radius 20
print(pi*20**2)
```
A different represenation:
```
import math

# Area of circle of radius 20
print(math.pi*20**2)
```

### Exercises:
1. Convert user input into an integer
2. Calculate the Area of a circle with radius 5.
    - declare all your variables as you would in algebra
    - import the math library
    - Steps 3: assign the value to the output of the circle formula
    - show in output using print
3. Get user input for radius, output the area  
4. Calculate the area of a triangle using [ ½ * base * height ] formula, from user input.
5. Find area of an Equilateral Triangle using the below formula: 

![alt text](https://github.com/djengineer/python_basics/blob/master/imgs/m2-area.png "Area 1")

where s is the length of one side of the triangle.
hint: look at the math reference if you are unsure
6. Find area of triangle using trigonometry:

![alt text](https://github.com/djengineer/python_basics/blob/master/imgs/m2-area2.png "Area 2")

where a = 12, b = 20, C = π/6

### Activity:  Cashier Checkout Program

Use what you have learnt so far to program a cashier checkout out program for a store which sells apples, pears and strawberries.

An apple sells for $1

A pear sells for $1.50

Strawberries sell for $2

The store gives 20% discount off the total price.

Bonus: draw a better looking cash register.

![alt text](https://github.com/djengineer/python_basics/blob/master/imgs/m2-cashier.png "Area 2")

# Module 3 : If / Else Conditional Statements

### Comparison Operators:
The output of a comparison will always return a True / False

| Operator      | Meaning       |
| ------------- |:-------------:|
| ==            | Equal to      |
| >             | More than     |
| >=            | More than or equal to     |
| <             | Less than        |
| <=            | Less than or equal to   |
| !=            | Not equal to      |

### Additional Logical operators

| Operator      |
| ------------- |
| AND           |
| OR            |
| NOT           |

### Boolean ( True/ False ) Operations

```
# declaring hungry is true
my_var = (1==1) # what is the value of my_var?
print(my_var)
```
## IF Statement

```
# declaring hungry is true
hungry = True
if hungry == True:
    print("let’s go have lunch")
```
Will it print successfully?
```
# declaring hungry is true
hungry = False
if hungry == True:
    print("let’s go have lunch")
```
Will anything be printed?

## Else statement

```
# declaring hungry is true
hungry = True
if hungry == True:
	Print("let’s go have lunch")
else:
	Print("let’s go play")
```
Which will be printed?

## If, Else if, Else

```
# declaring hungry is true
hungry = True
craving = "Pizza"
if hungry == True and craving=="Pizza":
	print("let’s go have pizza")
elif hungry == True and craving != "Pizza":
	print("let’s have something else") 
else: # not hungry
	print("let’s go play")
```
elif is short for "else if". We can have many "else if", but else is the last condition.
Else will be the check for all other conditions that we did not specify.

E.g. if craving equals something else, it will print "let's go play" too.

## Comparison logic not
```
hungry == True
print(not hungry) # what does the output become?
```
"Not" will reverse the True and return False, because False is Not True.

## Random number generator

```
from random import randint
# randint will generate a random integer
# randint(from_number, to_number)
number = randint(0,3)
print(number)
# generates a random integer between 0 and 3
```

## Exercises:
1. Find out if user input is Even or Odd number.
    1. get input from user
    2. convert input to integer
    3. use the modulo math operation to test for even or odd number
    4. show result in output using print
        Hint: use if,elif ,else conditions. Think about how you check for even or odd using modulo i.e. finding the remainder between what and what?
1.1.	Instead of asking the user for an input, use random to generate the initial number.
2.  Simple part of the program that asks users what they want to buy.
    1. get input from user 
    2. if user input == “a”, store user’s choice as apple. If user input == “p”, store user’s choice as pear, and if user input == “s”, store user’s choice as strawberries.
    3. print out the user’s choice.
3. Calculating probabilities: if user chooses apple, there is a 50% chance that that apples are sold out. 

## Activities:
1. Create a Role Playing Game (RPG) using input(), print(), and if/elif/else statements. Come up with an interesting story to entertain your player with!
You can even use math, and the random function to generate some interesting stories with probabilities in the game’s outcome!

# Module 5: Data Structure 1 - Lists

Lists are used to store multiple data into one variable.
Think of it as a shelf. We use square brackets to signify lists.

Declaring an empty list:
`my_list = []`

Declaring a list with data inside:
```
# A list is like a shelf with numbered spaces
# A list’s index starts from 0, e.g [0,1,2,3…]
# my_list[0] will call the first item in the list
my_list = ["pizza","noodles","burger","fries"]
print(my_list[0]) # this will give us "pizza"
print(my_list[3]) # this will give us "fries"
```

## List manipulation

```
mylist = [0,1,2,3,4]
print(mylist)
# append() is to add a value to the back of the list.
mylist.append(10)
print(mylist) # 10 is added to the back of the list
# len() is to find out the length of the list.
# in this case, it is how many elements are there.
print("Length of my list is",len(mylist))

# Slice of lists. Extract out values 
# elements 3rd to 5th
print("slicing from 3rd to 5th element:")
print(mylist[2:5])

# elements beginning to 4th,5 not included
print("slicing from beginning to 4th element:")
print(mylist[:4])

# elements 4th to end. Does not include the 3rd
print("slicing from 4th element to the end:")
print(mylist[3:])

# elements beginning to end
print("slicing from beginning to end:")
print(mylist[:])

# every second element using steps
print("Slicing every 2nd item in list")
print(mylist[::2])
# reverse elements
print("Slicing in a reverse step")
print(mylist[::-1])
```

## List manipulation 2

```
# Adding an element to the back of the list using append()
my_list = [10,20,30,40]
my_list.append(50)
print(my_list)
# Inserting an element into a certain position in the list using insert()
# insert 25 into index 2. Remember the first element in the list is index 0
# insert(index, object)
my_list.insert(2,25)
print(my_list)
# Sorting the values
sorted(my_list)
print(my_list)
print(sorted(my_list)) # notices sorted does not change the list itself.
# searching for an item in the list
shopping_list = ["apple","pear","milk","tea"]
If "milk" in shopping_list:
   print("Buy milk")
if "strawberry" not in shopping_list:
   shopping_list.append("strawberries")
# the not logic can be used here.
# can add an action if something is or is not in the list        
```

### Exercises:
1. Use list comprehension to declare a list my_list >> [0,1,2,3,4].
2. Add an integer 5 to the list
3. Add a float 2.345 between 4 and 5  
4. Sort my_list 

# Module 6: Loops

### For Loop
```
# Try this out
for i in range(10):
    print(i)
    print(i, "hello")
```
We can set specific ranges
```
# Try this out
for i in range(5,10):
    print(i, "hello")
```
We can skip steps. For example, we want it to print for every 2nd numnber

```
# Try this out
for i in range(0,10,2):
    print(i, "hello")
```
### While Loop

```
i = 0
while i < 10:
    print(i)
    i += 1 # add 1 to i itself
```
These two codes both do the same thing, but written in different ways.

## Looping through Lists

```
mylist = ["tom","harry","john"]
numberlist = [10,123,9,2,10]
for item in mylist:
    print(item)
print(" ")
# for each number in the list, print number
for number in numberlist:
    print(number)
```
## Nested Loops or "Loops within Loops
```
x = int(input("Enter a number for Range: "))
#int(variable) changes the string from input to integer
for i in range(x):
    for a in range(x):
        print(i,a)
```
Run the above and see what it does. i will stay the same while a increases. When a completes, i will increase by one and repeat the cycle.


## Nested loops with steps
```
# the parameters for range is range(start,end,step)
for i in range(0,4,2):
    for a in range(0,4,2):
        print(i,a)
```
## While Loop with Break

We can break out of a while loop when certain conditions are met.

```
hungry = True
while hungry == True: #infinite loop
    print("I had brunch")
    print("I am still hungry")
    print("I had snacks")
    hungry = False  # switch hungry to False
    if hungry == False:
        break   #this breaks out of the while loop
    print("I had dinner")
    print("Done - outside of loop")
```
## Example: a clock function

We print the current time every one second
```
# more on date time https://docs.python.org/3/library/time.html
import datetime
import time
today = datetime.date.today().strftime("%B %d, %Y")
print(today)
while True:
    # hour:minute:seconds
    time_now = datetime.datetime.now().strftime("%H:%M:%S")
    print(time_now)
    time.sleep(1)
```
The "datetime" library is used to get the date and time of the server.
the "time" library is used with a sleep function.
time.sleep(1) will pause the program for 1 second before continuing with the while loop.

## Exercises:
1. my_list = [0,1,2,3,4,3,2,1,0]. Use a for l¬¬¬¬oop to change the values to [1,2,3,4,5,4,3,2,1]
2. Use a for loop to change all the 3s in my_lists into 9s.
3. Use a for loop to multiply all the ¬¬4s by 8.
4. Use a for loop to sum all the items in my_list. Hint: use a separate variable
5. Use a for loop to find how many odd and even numbers in my_list
6. new_list = [10,20,30,40,50,60,70,80,90,100]. Use a for loop to print out every item in the list less than 74.
7. Use a for loop to print out the following tree, getting user inputs:
![alt text](https://github.com/djengineer/python_basics/blob/master/imgs/m6-xmastree.png "half triangle")

## Activity 1:
Change your right-angles triangle tree to look something like this. You can use * symbols in your last exercise.
![alt text](https://github.com/djengineer/python_basics/blob/master/imgs/m6-pyramid.png "pyramid")

