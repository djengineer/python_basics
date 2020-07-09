# Python Basics
Created by Wong Ding Jie
Copyright 2018 - 2020

# How to use this
Learners should follow the example code given and plug it into their own Python environment. Or learners can use online compilers like https://repl.it/

1. Run the code examples
2. Understand how it works
3. Try out the challenges
4. There are extra challenges at the very bottom if you finish your exercises fast.

# Introduction/Requirements
Python is used for many applications such as database, artificial intelligence, internet-of-things and many more.

File extension is **.py**

Python 3.6

Python 3.6 is compatible with PyGame.

Other resources:
IDLE - Default Python Integrated Environment (IDE))
Using PIP package manager for Python

If you install Python onto your own computer:
- https://www.python.org/downloads/release/python-369/
- https://www.python.org/downloads/

Once you installed Python3.6, you can use IDLE to run your codes.
To install PyGame, in the search bar on Windows, run cmd.exe.

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
hint: look at the math reference for how to do square root
https://docs.python.org/3/library/math.html

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
1. Find out if user input is Even or Odd number. (hint: a number modulo 2 will give 0 for even, and 1 for odd)
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

# Module 4: Data Structure 1 - Lists

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
1. Use list of 5 randomly generated numbers.
2. Add an integer 3 to the back of the list
3. insert a float 2.345 between 4th and 5th element  
4. Sort my_list 

# Module 5: Loops

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
1. my_list = [0,1,2,3,4,3,2,1,0]. Use a for loop to change the values to [1,2,3,4,5,4,3,2,1]
2. Use a for loop to change all the 3s in my_lists into 9s.
3. Use a for loop to multiply all the 4s by 8.
4. Use a for loop to sum all the items in my_list. Hint: use a separate variable
5. Use a for loop to find how many odd and even numbers in my_list
6. new_list = [10,20,30,40,50,60,70,80,90,100]. Use a for loop to print out every item in the list less than 74.
7. Use a for loop to print out the following tree, getting user inputs:
![alt text](https://github.com/djengineer/python_basics/blob/master/imgs/m6-xmastree.png "half triangle")

## Activity 1:
Change your right-angles triangle tree to look something like this. You can use * symbols in your last exercise.
![alt text](https://github.com/djengineer/python_basics/blob/master/imgs/m6-pyramid.png "pyramid")

# Module 6: Data Structures 2 - 2D Lists and Disctionaries
## Multi-dimensional lists / 2D-Arrays

Two-dimensional arrays can be used to represent a chess board for example.

```
# A multidimensional list is a list within a list
# also called a multidimensional array
#
# recall matrix and matrices your mathematics
# a 2x2 matrix
# index positions look like this
# | [0][0] , [0][1] |
# | [1][0] , [1][1] |

multi_list = [
                [1,2],
                [3,4]
             ]
print(multi_list[0][0])
print(multi_list[0][1])
print(multi_list[1][0])
print(multi_list[1][1])
multi_list.append([5,6])
print("The multi list now has 3 list elements")
print(multi_list)
print("Print out the newly appended list")
print(multi_list[2][0])
print(multi_list[2][1])
```
### Looping through a 2D-array

E.g. This code will print out the items in the 2D list in order.
```
multi_list = [
                [1,2],
                [3,4]
             ]
# to print out all values in order, like the prev codes
for row in multi_list:
    for cell_value in row:
        print(cell_value)
	
# But what if we want to change the cell value??
# to change the value
multi_list[0][1] = "hello"
# this changes the value at position [0][1] to "hello"
print(multi_list)
```
We can use this to replace elements if we do not know their position.
E.g. This code has a "hello" at [0][1]. 
1. We loop through the whole list
2. if the element matches "hello"
3. Change the element to "world"
```
#We want to loop through list, find "hello" and replace it with "world"
multi_list = [
                [1,"hello"],
                [3,4]
             ]
# the for loop previously does not include an index
# for us to use a 2D-array like mylist[i]
# we need to generate the index to get the index

for i, row in enumerate(multi_list):
    for j, cell in enumerate(row):
        if cell == "hello":
            multi_list[i][j] = "world" 
        print(multi_list[i][j]) # print after changing
	
# we just used a for loop to run through the 
# 2D Array, searching for "hello" and changing it to "world"
```
## Dictionary Data type

Dictionary type has a "key" and a "value", forming what we call a "key-value" pair.

### Using Dictionaries
```
# dictionaries data structures
# relationship between dictionaries and lists
empty_dictionary = {}
empty_list = []
my_list = ["Good Morning from list"]

# my_dict = { key : value }
# we call this a key-value pair.
my_dict = {"greeting_1":"Good Morning from dictionary"}

# to print good morning
print(my_list[0])

# unlike lists, there is no indexing in dictionaries,
# we find the value by searching in the dictionary with the key
# in this case we are printing the value of the greeting_1 key
print(my_dict["greeting_1"])

# to add to the list and dictionary
my_list.append("Good Afteroon")
my_dict["greeting_2"] = "Good Afternoon"

# confirm contents 
print(my_list)
print(my_dict)

# to print good afternoon
print(my_list[1])
print(my_dict["greeting_2"])

# we can have a list of dictionaries and a dictionary of lists
```
## Exercises:

1.	Declare and empty 2D array  multi_list = [[],[],[]]
2.	Use a nested for loop to populate the list [0,1,2,3] for each row.
3.	[Challenge] For each cell in the 2D array, change the integers into string i.e. 0 => “zero”, 1 => ”one” , 2 => “two”

# Module 7: Functions
Functions are reusable block of codes.
They take in some arguments(values), process it and returns a value to the main program.

## Defining a function
```
# define our function
def my_func():
    print("hello function")
# Run the program. Is anything printed in the shell?
# To use the function, we must call our function.
my_func()
# is it printed out now?

```
## Passing data into functions
We can pass values into a function.
We must call a function.
```
# my_func is set to take in a variable that 
# we will name my_string
def my_func(my_string):
    print("Hello function")
    print(my_string)
# does calling the function run?
my_func()
# we must parse in the parameters when we call the function
my_func("this is the string that I will parse")
```
The above will have error at line 7. my_func() did not pass any value, even though the function is expecting something.\
We erase line 7 and try again.
```
# my_func is set to take in a variable that 
# we will name my_string
def my_func(my_string):
    print("Hello function")
    print(my_string)

# we must parse in the parameters when we call the function
my_func("this is the string that I will parse")
```
### Practical example: Calculator functions
```
# define function
# the variables i and j are only used within this function
# i and j takes the values from the 2 parameters that is parsed

def addition(i,j):
    print("The sum of the 2 numbers are",i+j)
    
# start of main program

print("To add 2 numbers:")
a = input("Enter first number: ")
b = input("Enter second number: ")

# input is stored as a string
# we need to change it to a number.
# we parse the 2 variables a and b

addition(int(a),int(b))

# notice that the variables a and b 
# is now referred to as i and j in the function 
# a is mapped to i, and b is mapped to j
```
### Returning a value to the main program
```
# what if we want to store the output of a function
# into a variable in the main program?

def addition(i,j):
    output = i+j
    return(output)
    
# we can also write it as return(i+j)
# For clarity we put it into output variable first
# start of main program

print("To add 2 numbers:")
a = input("Enter first number: ")
b = input("Enter second number: ")

# the function will return the value to the main program

result = addition(int(a),int(b))

# output of addition function is stored in result

print("The sum of the 2 numbers are",result)
```
## Exercises:
1.	Let’s create a simple cashier checkout program using functions for an apple shop. Each apple costs $0.80. If total purchase is more than $10, give 50% discount off the total purchase 
2.	Gather user input asking for how many apples the user would like to buy.
3.	Define a function, called calc_cost, to calculate the total cost. Use parameter parsing and return value to save the output of the function into a variable called total_purchase.
4.	Define a function, called check_eligible, to check if the purchase is eligible for the discount. Return a True/False to the main program to a variable called is_eligible
5.	If is_eligible is True, calculate and show the final_price, else show the price without discount 
6.	Trying using the check_eligible function from within the calc_cost function

# Module 8: Introduction to PyGame and game design

PyGame is a library that we can use to create apps with Graphical User Interface.

### Basic example with a white screen
```
import pygame

pygame.init()
pygame.font.init()
myfont = pygame.font.SysFont("monospace", 60)
size = (600,300)
screen = pygame.display.set_mode(size)
bgcolor = (255,255,255)
screen.fill(bgcolor)
label = myfont.render("hello", 1, (0,0,0))
screen.blit(label, (100, 100))    
pygame.display.flip()

```
#### Try and answer the following questions:
- Where do you think we can change the text?
- How do we change the size of the screen?
- where do we change background color?
- where do we change font color?

Colors are in RGB where (0,0,0) is black, and (255,255,255) is white.
We can use this link for color picker
https://www.w3schools.com/colors/colors_picker.asp

Choose the RGB values

## Game Loop and status flags
The game loop is used to control start and stop of the game.
We use status flags to keep track of the status of the game.
```
# The basic game loop looks like this

done = False
while done == False:
    print("Game is running")    
while done == True:
    quit() # quit() is to quite the python shell

```
### Changing the flags
```
while done == False:
    print("Game is running")
    user_input = input("To quit, enter (q): ")
    if user_input == "q":
        # we change the flag to True
        # once the flag changes to True, the program will jump
        # to the next section of the code where done == True
        print("quit game")
        done = True
```
### Putting in menus into our app
```
# initialize
done = False
# first page is of the game is the main menu
# thats why we initialize it before the game loop starts
main_menu = True
while done == False:
    print("Game is running")
    # if we are in the main menu
    if main_menu == True:
        print("This is the game menu:")
        # get user to choose from the menu
        user_choice = input("Choose between 2 options (A/B): ")
        # run the program for each option chosen
        if user_choice == "A":
            print("Run Option A")
        elif user_choice == "B":
            print("Run Option B")
        else:
            user_choice = input("Choose between 2 options (A/B): ")
    user_input = input("To quit, enter (q): ")
    if user_input == "q":
        print("quit game")
        done = True

```
### Using functions

If we put the whole chunk of menu code into a function, we can make our codes look cleaner
```
# initialize

done = False

# first page is of the game is the main menu
# thats why we initialize it before the game loop starts

main_menu = True

def menu_function():
  print("This is the game menu:")
  
  # get user to choose from the menu
  user_choice = input("Choose between 2 options (A/B): ")
  
  # run the program for each option chosen
  if user_choice == "A":
      print("Run Option A")
  elif user_choice == "B":
      print("Run Option B")
  else:
      user_choice = input("Choose between 2 options (A/B): ")

######## Main Game Loop Here ##########

while done == False:
    print("Game is running")
    # if we are in the main menu
    if main_menu == True:
        menu_function()
    user_input = input("To quit, enter (q): ")
    if user_input == "q":
        print("quit game")
        done = True
```

## Activity
Make your own clock app

1. We know how to get the current time
2. We know where to display text
3. Start simple, we don't need any menus
4. Combine the basic pygame example with the game loop
5. Revisit our clock function in module 6.

# EXTRA Challenges

1. Build your own hangman word game.
2. Build a rock-paper-scissors game.
3. Spice up your clock with an image background, background music or however else you wish to build.
https://www.pygame.org/docs/ref/image.html
https://www.pygame.org/docs/ref/mixer.html

Challenge yourself. If you are stuck, you can find my solutions uploaded as well.

The end =============================
