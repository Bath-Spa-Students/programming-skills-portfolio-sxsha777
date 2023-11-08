'''Write a loop that prompts the user to enter a series of pizza toppings until 
they enter a 'quit' value. As they enter each topping, print a message saying 
you'll add that topping to their pizza.'''

while True:
    print("\n")
    pizza_topping = input("What kind of pizza topping would you like?? ")
    if pizza_topping == "quit":
        break
    print("I will add the ", pizza_topping, " topping to your pizza")