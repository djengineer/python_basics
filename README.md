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
