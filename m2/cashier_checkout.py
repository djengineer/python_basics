apple_price = 1           #in dollars
pear_price = 1.50
strawberry_price = 2
print("---- ---- ----")
print("|   Cashier   |")
print("|    Here     |")
print("---- ---- ----")

apple_amount = int(input("How many apples do you want?"))
pear_amount = int(input("How many pear do you want?"))
strawberry_amount = int(input("How many strawberries do you want?"))

totalprice = apple_price * apple_amount \
            + pear_price * pear_amount  \
            + strawberry_price * strawberry_amount 
#backslashes help format the lines to see it clearer

totalprice_discount = totalprice * 0.8
print("Total discounted price is",totalprice_discount)
