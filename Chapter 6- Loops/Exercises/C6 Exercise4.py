'''Make a list called sandwich_orders and fill it with the names of various sandwiches. 
Then make an empty list called finished_sandwiches.
Loop through the list of sandwich orders and print a message for each order, such as 
"I made your tuna sandwich". As each sandwich is made, move it to the list of finished sandwiches. 
After all the sandwiches have been made, print a message listing each sandwich that was made.'''

sandwich_orders = ['veg', 'grilled cheese', 'club', 'wrap']
finished_sandwiches = []
while sandwich_orders:
    sandwich_wip = sandwich_orders.pop()
    print (sandwich_wip, "is being made.")
    finished_sandwiches.append(sandwich_wip)

for i in finished_sandwiches:
    print("I made your", i, "sandwich.")