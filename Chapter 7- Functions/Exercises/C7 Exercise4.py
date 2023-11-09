'''Modify the make_shirt() function so that shirts are large by default with 
a message that reads I love Python. 
Make a large shirt and a medium shirt with the default message, and a shirt 
of any size with a different message.'''

def make_shirt(size="Large",message="I love Python."):
    print("Shirt Summary.")
    print("Shirt size will be: ", size)
    print("Message on the shirt is: ", message)
    print("\n")

make_shirt()
make_shirt(size="Medium")
make_shirt("Small", "Stay fearless.")

