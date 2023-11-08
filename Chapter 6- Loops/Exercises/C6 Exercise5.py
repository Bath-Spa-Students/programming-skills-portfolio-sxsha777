'''Using the list sandwich_orders from Exercise 7-8, make sure the sandwich 'pastrami' 
appears in the list at least three times. Add code near the beginning of your program 
to print a message saying the deli has run out of pastrami, and then use a while loop to 
remove all occurrences of 'pastrami' from sandwich_orders. Make sure no pastrami sandwiches 
end up in finished_sandwiches.'''

sandwich_orders=["veg", "grilled cheese", "pastrami", "pastrami",
    "wrap", "club", "pastrami"]
finished_sandwiches=[]

print("Sorry, we're out of pastrami today.")
while 'pastrami' in sandwich_orders:
    sandwich_orders.remove("pastrami")
print("\n")

while sandwich_orders:
    current=sandwich_orders.pop()
    print("Working on your", current, "sandwich.")
    finished_sandwiches.append(current)
print("\n")

for i in finished_sandwiches:
    print("Your", i, "sandwich has been made.")