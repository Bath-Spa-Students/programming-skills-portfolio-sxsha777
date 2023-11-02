'''Now that you know how to loop through a dictionary, clean up the code from Exercise 6-3 
(page 99) by replacing your series of print() calls with a loop that runs through the 
dictionary's keys and values.
When you're sure that your loop works, add five more Python terms to your glossary.
When you run your program again, these new words and meanings should automatically be included 
in the output.'''

recap={"String": "A series of characters.", "Strip": "Function used to remove white spaces",
"Comments": "Short descriptions alongside code.", "Input": "Allows user to input value.",
"Variable": "Containers that are used to store data."}

for x,y in recap.items():
    print(x, ": " + y, "\n")