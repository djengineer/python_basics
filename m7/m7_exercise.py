# call the checkout program using 3 functions
# to initialize variables -> var_init()
# to get user inputs -> user_input()
#   put user input into a dictionary
#       and return the list to main program
# to calculate -> calculate()

def var_init():
    global apple_price
    global pear_price
    global strawberry_price
    apple_price = 1           #in dollars
    pear_price = 1.50
    strawberry_price = 2
    print("---- ---- ----")
    print("|   Cashier   |")
    print("|    Here     |")
    print("---- ---- ----")

def user_input():
    apple_amount = int(input("How many apples do you want?"))
    pear_amount = int(input("How many pear do you want?"))
    strawberry_amount = int(input("How many strawberries do you want?"))
    output = {"a_amt":apple_amount,"p_amt":pear_amount,"s_amt": strawberry_amount}    
    return(output)

def calculate(apple_amount,pear_amount,strawberry_amount):
    totalprice = apple_price * apple_amount \
                + pear_price * pear_amount  \
                + strawberry_price * strawberry_amount 
    #backslashes help format the lines to see it clearer
    totalprice_discount = totalprice * 0.8
    print("Total price is $",totalprice_discount)

var_init()
amount = user_input()
# remember that the sequence is important
calculate(amount["a_amt"],amount["p_amt"],amount["s_amt"])
