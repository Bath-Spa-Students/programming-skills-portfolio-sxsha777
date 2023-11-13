'''Write a python program with nested decision structures that perform the following: If amount1
is greater than 10 and amount2 is less than 100, display the greater of amount1 and amount2'''

amount1=int(input("Enter first amount: "))
amount2=int(input("Enter second amount: "))
if amount1 > 10 and amount2 < 100:
    if amount1 > amount2:
        print("amount1 is greater than amount2")
    elif amount2 > amount1:
        print("amount2 is greater than amount1")
else:
    print("invalid amounts.")