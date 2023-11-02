'''Make a dictionary containing three major rivers and the country each river runs through. 
One key-value pair might be 'nile': 'egypt'.
* Use a loop to print a sentence about each river, such as The Nile runs through Egypt.
* Use a loop to print the name of each river included in the dictionary.
* Use a loop to print the name of each country included in the dictionary.'''

rivers={"Nile": "Egypt", "Ganga": "India", "Amazon": "USA", "Volga": "Russia", "Yangtze": "China"}
for r,c in rivers.items():
     print("The", r, "runs through", c, ".")

print("\n", "The rivers included in this dictionary:")
for r in rivers.keys():
    print("* ", r)

print("\n", "The countries included in this dictionary: ")
for c in rivers.values():
    print("* " + c)

