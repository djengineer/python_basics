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


def check_elidgible(total_price):
    if total_price > 10:
        return True
    else:
        return False

def calculate(apple_amount,pear_amount,strawberry_amount):
    totalprice = apple_price * apple_amount \
                + pear_price * pear_amount  \
                + strawberry_price * strawberry_amount 
    #backslashes help format the lines to see it clearer
    if check_elidgible(totalprice) == True:
        totalprice_discount = totalprice * 0.5
        print("Price is discounted")
        print("Total price is $",totalprice_discount)
    else:
        print("No discount given")
        print("Total price is $",totalprice)


## main program here
var_init()
amount = user_input()
# remember that the sequence is important
calculate(amount["a_amt"],amount["p_amt"],amount["s_amt"])
